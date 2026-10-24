# Single-phase power

Category: Power. Calculator ID: `single_power`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | RMS voltage | 230 | V |
| `current` | RMS line current | 10 | A |
| `pf` | Displacement power factor (lagging) | 0.8 | pu |

## Derivation

1. `S = V I`
2. `P = S pf`
3. `Q = S sqrt(1 - pf²)`

## Reference outputs

- `apparent` = 2300 VA
- `active` = 1840 W
- `reactive` = 1380 var

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate single_power --inputs '{"voltage": 230, "current": 10, "pf": 0.8}'
python -m unittest tests.test_calc_single_power
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
