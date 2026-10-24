from importlib import import_module
from pathlib import Path
from functools import lru_cache

@lru_cache(maxsize=1)
def calculators():
    result = {}
    for path in sorted((Path(__file__).parent/'calculators').glob('c_*.py')):
        calc = import_module('powercalcs.calculators.' + path.stem).CALCULATOR
        if calc.id in result:
            raise RuntimeError('Duplicate calculator: ' + calc.id)
        result[calc.id] = calc
    return result

def calculate(name, inputs):
    try:
        calc = calculators()[name]
    except KeyError as exc:
        raise ValueError('Unknown calculator: ' + name) from exc
    return calc.run(inputs)
