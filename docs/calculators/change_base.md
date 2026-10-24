# Change per-unit impedance base

Category: Transformers. Calculator ID: `change_base`.

Same physical impedance and winding side. Magnitude-only conversion; impedance angle remains unchanged.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `impedance` | Impedance magnitude on old base | 0.1 | pu |
| `old_power` | Old base apparent power | 1000000.0 | VA |
| `new_power` | New base apparent power | 2000000.0 | VA |
| `old_voltage` | Old line voltage base | 11000 | V |
| `new_voltage` | New line voltage base | 11000 | V |

## Derivation

1. `Z_pu,new = Z_pu,old (S_new/S_old) (V_old/V_new)²`

## Reference outputs

- `new_impedance` = 0.2 pu

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate change_base --inputs '{"impedance": 0.1, "old_power": 1000000.0, "new_power": 2000000.0, "old_voltage": 11000, "new_voltage": 11000}'
python -m unittest tests.test_calc_change_base
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
