# Motor full-load electrical current

Category: Motors. Calculator ID: `motor_full_load`.

Balanced three-phase motor at the specified operating efficiency and displacement power factor.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `shaft_power` | Mechanical shaft output | 15000 | W |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `efficiency` | Efficiency | 0.9 | pu |
| `pf` | Power factor | 0.85 | pu |

## Derivation

1. `P_input = P_shaft / eta`
2. `I_L = P_input / (sqrt(3) V_LL pf)`
3. `P_loss = P_input - P_shaft`

## Reference outputs

- `input_power` = 16666.666666666668 W
- `current` = 28.301483783805185 A
- `losses` = 1666.666666666668 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate motor_full_load --inputs '{"shaft_power": 15000, "voltage": 400, "efficiency": 0.9, "pf": 0.85}'
python -m unittest tests.test_calc_motor_full_load
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
