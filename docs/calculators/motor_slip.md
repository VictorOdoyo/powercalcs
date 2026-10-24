# Induction motor slip

Category: Motors. Calculator ID: `motor_slip`.

Signed slip permits generating operation when rotor speed exceeds synchronous speed; rotor frequency is a magnitude.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `sync_speed` | Synchronous speed | 1500 | rpm |
| `rotor_speed` | Rotor mechanical speed | 1440 | rpm |
| `frequency` | Frequency | 50 | Hz |

## Derivation

1. `s = (n_sync - n_rotor) / n_sync`
2. `slip (%) = 100 s`
3. `f_rotor = |s| f_supply`

## Reference outputs

- `slip` = 0.04 pu
- `slip_percent` = 4 %
- `rotor_frequency` = 2 Hz

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate motor_slip --inputs '{"sync_speed": 1500, "rotor_speed": 1440, "frequency": 50}'
python -m unittest tests.test_calc_motor_slip
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
