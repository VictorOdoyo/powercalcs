# Three-phase feeder voltage drop

Category: Cables. Calculator ID: `three_voltage_drop`.

First-order longitudinal drop approximation, sinusoidal lagging load. R and X are per conductor per metre; length is one-way. Three-phase case is balanced; single-phase has identical outgoing and return conductors.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `current` | RMS line current | 10 | A |
| `resistance` | Per-conductor resistance per metre | 0.0005 | ohm/m |
| `reactance` | Per-conductor reactance per metre | 8e-05 | ohm/m |
| `length` | One-way route length | 100 | m |
| `pf` | Displacement power factor (lagging) | 0.8 | pu |

## Derivation

1. `dV = sqrt(3) I L (R pf + X sqrt(1-pf²))`
2. `drop (%) = 100 dV / V`
3. `V_receiving approximately V - dV`

## Reference outputs

- `drop` = 0.775958761790857 V

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate three_voltage_drop --inputs '{"voltage": 400, "current": 10, "resistance": 0.0005, "reactance": 8e-05, "length": 100, "pf": 0.8}'
python -m unittest tests.test_calc_three_voltage_drop
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
