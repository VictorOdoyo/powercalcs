# Three-phase voltage

Category: Power. Calculator ID: `three_voltage`.

Total active electrical power; three-phase output is balanced line-to-line voltage.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `current` | RMS current | 10 | A |
| `pf` | Power factor | 0.8 | pu |

## Derivation

1. `V = P / (sqrt(3) I pf)`

## Reference outputs

- `voltage` = 721.6878364870322 V

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate three_voltage --inputs '{"power": 10000, "current": 10, "pf": 0.8}'
python -m unittest tests.test_calc_three_voltage
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
