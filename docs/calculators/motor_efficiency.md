# Motor efficiency and losses

Category: Motors. Calculator ID: `motor_efficiency`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `input_power` | Electrical input power | 10000 | W |
| `output_power` | Mechanical output power | 9000 | W |

## Derivation

1. `eta = P_output / P_input`
2. `losses = P_input - P_output`

## Reference outputs

- `efficiency` = 0.9 pu
- `percent` = 90 %
- `losses` = 1000 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate motor_efficiency --inputs '{"input_power": 10000, "output_power": 9000}'
python -m unittest tests.test_calc_motor_efficiency
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
