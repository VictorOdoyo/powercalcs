# Motor starting current

Category: Motors. Calculator ID: `motor_start_current`.

Specified starting-current multiple; ignores acceleration, voltage dependence, and starter dynamics.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `current` | RMS line current | 10 | A |
| `multiple` | Locked-rotor current multiple | 6 | pu |

## Derivation

1. `I_start = multiple I_full_load`

## Reference outputs

- `starting_current` = 60 A

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate motor_start_current --inputs '{"current": 10, "multiple": 6}'
python -m unittest tests.test_calc_motor_start_current
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
