# Symmetrical components

Category: Phasors. Calculator ID: `symmetrical_components`.

ABC positive sequence; RMS voltage phasors use exp(j omega t). Input angles may be degrees or radians.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `a_mag` | A magnitude | 230 | V |
| `a_angle` | A angle | 0 | deg |
| `b_mag` | B magnitude | 230 | V |
| `b_angle` | B angle | -120 | deg |
| `c_mag` | C magnitude | 230 | V |
| `c_angle` | C angle | 120 | deg |

## Derivation

1. `a = exp(j 120 degrees)`
2. `V0 = (VA + VB + VC) / 3`
3. `V1 = (VA + a VB + a² VC) / 3`
4. `V2 = (VA + a² VB + a VC) / 3`

## Reference outputs

- `zero` = [0, 0] V
- `positive` = [230, 0] V
- `negative` = [0, 0] V

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate symmetrical_components --inputs '{"a_mag": 230, "a_angle": 0, "b_mag": 230, "b_angle": -120, "c_mag": 230, "c_angle": 120}'
python -m unittest tests.test_calc_symmetrical_components
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
