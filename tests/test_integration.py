import json
import math
import subprocess
import sys
import threading
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer
from powercalcs.catalog import calculate,calculators
from powercalcs.phasors import reconstruct,sequences
from powercalcs.server import Handler
from powercalcs.units import convert

class EngineProperties(unittest.TestCase):
    def defaults(self,name):
        return {f.key:f.default for f in calculators()[name].fields}

    def test_all_default_cases_produce_finite_outputs(self):
        self.assertEqual(len(calculators()),50)
        for name in calculators():
            with self.subTest(calculator=name):
                result=calculate(name,self.defaults(name))
                self.assertEqual(set(result['results']),set(result['output_units']))
                json.dumps(result,allow_nan=False)

    def test_unit_equivalence_and_dimension_rejection(self):
        inputs=self.defaults('three_power')
        inputs['voltage']={'value':.4,'unit':'kV'}
        self.assertAlmostEqual(calculate('three_power',inputs)['results']['active'],5542.562584220407)
        inputs['voltage']={'value':400,'unit':'A'}
        with self.assertRaisesRegex(ValueError,'dimension'):
            calculate('three_power',inputs)

    def test_nonfinite_and_boolean_inputs_rejected(self):
        for value in [math.nan,math.inf,-math.inf,True,'400',None,{},[]]:
            with self.subTest(value=value):
                inputs=self.defaults('three_power');inputs['voltage']=value
                with self.assertRaises(ValueError): calculate('three_power',inputs)

    def test_unknown_input_and_calculator_rejected(self):
        with self.assertRaisesRegex(ValueError,'Unknown calculator'): calculate('missing',{})
        inputs=self.defaults('single_power');inputs['typo']=1
        with self.assertRaisesRegex(ValueError,'Unknown inputs'): calculate('single_power',inputs)

    def test_zero_current_zero_power(self):
        inputs=self.defaults('three_power');inputs['current']=0
        self.assertEqual(calculate('three_power',inputs)['results']['active'],0)

    def test_invalid_domains(self):
        cases=[('three_current','pf',0),('three_power','pf',1.1),('three_power','voltage',-1),('synchronous_speed','poles',3),('synchronous_speed','poles',2.5),('motor_efficiency','output_power',11000),('pf_correction','target_pf',.7),('pf_from_power','apparent',5000)]
        for name,key,value in cases:
            with self.subTest(calculator=name,key=key):
                inputs=self.defaults(name);inputs[key]=value
                with self.assertRaises(ValueError):calculate(name,inputs)

    def test_floating_neutral_kirchhoff(self):
        inputs=self.defaults('star_floating');inputs.update(xa=2,xb=-3,xc=5)
        result=calculate('star_floating',inputs)['results']
        current=sum(complex(result[k]['real'],result[k]['imag']) for k in ['ia','ib','ic'])
        self.assertLess(abs(current),1e-10)

    def test_delta_line_currents_sum_to_zero(self):
        result=calculate('delta_unbalanced',self.defaults('delta_unbalanced'))['results']
        current=sum(complex(result[k]['real'],result[k]['imag']) for k in ['ia','ib','ic'])
        self.assertLess(abs(current),1e-10)

    def test_sequence_round_trip(self):
        for phases in [(230+12j,-100-180j,-110+200j),(0j,0j,0j),(10j,20j,30j)]:
            recovered=reconstruct(*sequences(*phases))
            for a,b in zip(phases,recovered):self.assertLess(abs(a-b),1e-10)

    def test_star_delta_capacitance_ratio(self):
        star=calculate('star_capacitance',self.defaults('star_capacitance'))['results']['capacitance_per_phase']
        delta=calculate('delta_capacitance',self.defaults('delta_capacitance'))['results']['capacitance_per_phase']
        self.assertAlmostEqual(star,3*delta)

    def test_per_unit_base_identity(self):
        inputs=self.defaults('change_base');inputs['new_power']=inputs['old_power']
        self.assertAlmostEqual(calculate('change_base',inputs)['results']['new_impedance'],.1)

    def test_si_geometry_units(self):
        inputs=self.defaults('conductor_resistance');inputs['area']={'value':25,'unit':'mm2'}
        self.assertAlmostEqual(calculate('conductor_resistance',inputs)['results']['resistance'],.06896)

    def test_angle_provenance_uses_normalized_radians(self):
        inputs=self.defaults('symmetrical_components')
        result=calculate('symmetrical_components',inputs)
        self.assertEqual(result['input_units']['b_angle'],'rad')
        self.assertAlmostEqual(result['inputs_si']['b_angle'],-2*math.pi/3)
        inputs['b_angle']={'value':-2*math.pi/3,'unit':'rad'}
        converted=calculate('symmetrical_components',inputs)
        self.assertAlmostEqual(converted['results']['positive']['real'],230)

    def test_unit_name_must_be_a_string(self):
        for unit in [[],{},None,1]:
            with self.subTest(unit=unit), self.assertRaises(ValueError):
                convert(1,unit,'voltage')

    def test_integer_counts_accept_integral_numeric_values(self):
        inputs=self.defaults('synchronous_speed')
        for poles in [4,4.0,{'value':4,'unit':'count'}]:
            with self.subTest(poles=poles):
                inputs['poles']=poles
                self.assertEqual(calculate('synchronous_speed',inputs)['results']['speed'],1500)

    def test_capacitive_reactive_power_is_negative(self):
        inputs=self.defaults('balanced_star');inputs['reactance']=-1
        self.assertLess(calculate('balanced_star',inputs)['results']['reactive'],0)

    def test_uncertainty_zero_limit(self):
        inputs=self.defaults('power_uncertainty');inputs.update(u_voltage=0,u_current=0,u_pf=0)
        self.assertEqual(calculate('power_uncertainty',inputs)['results']['expanded_uncertainty'],0)

    def test_overflow_and_invalid_unit(self):
        with self.assertRaises(ValueError):convert(1e308,'MW','power')
        with self.assertRaises(ValueError):convert(1,'unknown','voltage')

class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.base=f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def test_assets_and_catalog(self):
        for path in ['/','/style.css','/app.js','/api/catalog']:
            with self.subTest(path=path),urlopen(self.base+path) as response:
                self.assertEqual(response.status,200)
                self.assertIn('nosniff',response.headers['X-Content-Type-Options'])
                self.assertGreater(len(response.read()),100)

    def test_calculate_and_reject_bad_json(self):
        body=json.dumps({'calculator':'single_power','inputs':{'voltage':230,'current':10,'pf':.8}}).encode()
        request=Request(self.base+'/api/calculate',data=body,headers={'Content-Type':'application/json'})
        with urlopen(request) as response:self.assertEqual(json.load(response)['results']['active'],1840)
        request=Request(self.base+'/api/calculate',data=b'{invalid',headers={'Content-Type':'application/json'})
        with self.assertRaises(HTTPError) as caught:urlopen(request)
        self.assertEqual(caught.exception.code,400)

    def test_cross_origin_rejected(self):
        request=Request(self.base+'/api/calculate',data=b'{}',headers={'Content-Type':'application/json','Origin':'https://example.com'})
        with self.assertRaises(HTTPError) as caught:urlopen(request)
        self.assertEqual(caught.exception.code,403)

    def test_path_traversal_is_not_a_file_server(self):
        with self.assertRaises(HTTPError) as caught:urlopen(self.base+'/../pyproject.toml')
        self.assertEqual(caught.exception.code,404)

class CLITests(unittest.TestCase):
    def test_list(self):
        result=subprocess.run([sys.executable,'-m','powercalcs','list'],capture_output=True,text=True,check=True)
        self.assertEqual(len(json.loads(result.stdout)),50)

    def test_calculation_from_stdin(self):
        result=subprocess.run([sys.executable,'-m','powercalcs','calculate','single_power','--file','-'],input='{"voltage":230,"current":10,"pf":0.8}',capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout)['results']['active'],1840)

    def test_invalid_name_is_structured_error(self):
        result=subprocess.run([sys.executable,'-m','powercalcs','calculate','nope','--inputs','{}'],capture_output=True,text=True)
        self.assertEqual(result.returncode,2);self.assertIn('error',json.loads(result.stderr))
