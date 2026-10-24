# Three-phase power

Category: Power. Calculator ID: `three_power`.

Balanced three-phase sinusoidal load. Voltage is line-to-line; current is line current. Lagging power factor.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `current` | RMS line current | 10 | A |
| `pf` | Displacement power factor (lagging) | 0.8 | pu |

## Derivation

1. `S = sqrt(3) V_LL I_L`
2. `P = S pf`
3. `Q = S sqrt(1 - pf²)`

## Reference outputs

- `apparent` = 6928.203230275509 VA
- `active` = 5542.562584220407 W
- `reactive` = 4156.921938165305 var

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate three_power --inputs '{"voltage": 400, "current": 10, "pf": 0.8}'
python -m unittest tests.test_calc_three_power
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
