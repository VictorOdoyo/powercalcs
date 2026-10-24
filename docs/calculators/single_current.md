# Single-phase current

Category: Power. Calculator ID: `single_current`.

Sinusoidal load. Three-phase option assumes balance and line-to-line voltage. Active power is total electrical input.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `voltage` | RMS voltage | 230 | V |
| `pf` | Displacement power factor | 0.8 | pu |

## Derivation

1. `I = P / (1 V pf)`

## Reference outputs

- `current` = 54.34782608695652 A

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate single_current --inputs '{"power": 10000, "voltage": 230, "pf": 0.8}'
python -m unittest tests.test_calc_single_current
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
