# Power triangle

Category: Power. Calculator ID: `power_triangle`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `reactive` | Signed reactive power | 7500 | var |

## Derivation

1. `S = sqrt(P² + Q²)`
2. `pf = P / S`
3. `phi = atan2(Q, P)`

## Reference outputs

- `apparent` = 12500 VA
- `pf` = 0.8 pu
- `angle` = 36.86989764584402 deg

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate power_triangle --inputs '{"power": 10000, "reactive": 7500}'
python -m unittest tests.test_calc_power_triangle
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
