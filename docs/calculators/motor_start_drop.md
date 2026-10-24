# Motor starting feeder drop

Category: Motors. Calculator ID: `motor_start_drop`.

First-order balanced feeder drop at fixed specified starting current; R/X are total per-phase feeder impedances. Does not solve voltage-dependent motor starting or acceleration.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `start_current` | Starting RMS current | 300 | A |
| `resistance` | Resistance | 1 | ohm |
| `reactance` | Reactance (+ inductive) | 1 | ohm |
| `start_pf` | Starting lagging power factor | 0.35 | pu |

## Derivation

1. `dV approximately sqrt(3) I_start (R pf_start + X sqrt(1-pf_start²))`

## Reference outputs

- `drop` = 668.6037188883105 V

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate motor_start_drop --inputs '{"voltage": 400, "start_current": 300, "resistance": 1, "reactance": 1, "start_pf": 0.35}'
python -m unittest tests.test_calc_motor_start_drop
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
