# Two parallel feeder current sharing

Category: Cables. Calculator ID: `parallel_feeders`.

Two uncoupled branches with common terminals; total current is the zero-angle reference phasor. Mutual impedance omitted.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `current` | RMS line current | 10 | A |
| `r1` | Feeder 1 resistance | 1 | ohm |
| `x1` | Feeder 1 reactance | 0 | ohm |
| `r2` | Feeder 2 resistance | 2 | ohm |
| `x2` | Feeder 2 reactance | 0 | ohm |

## Derivation

1. `I1 = I_total Z2 / (Z1 + Z2)`
2. `I2 = I_total Z1 / (Z1 + Z2)`
3. `P_loss = |I1|² R1 + |I2|² R2`

## Reference outputs

- `i1` = [6.666666666666667, 0] A
- `i2` = [3.3333333333333335, 0] A
- `loss` = 66.66666666666667 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate parallel_feeders --inputs '{"current": 10, "r1": 1, "x1": 0, "r2": 2, "x2": 0}'
python -m unittest tests.test_calc_parallel_feeders
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
