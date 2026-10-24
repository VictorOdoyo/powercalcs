# Three-phase power measurement uncertainty

Category: Studies. Calculator ID: `power_uncertainty`.

First-order independent standard uncertainties; covariance is zero. Coverage factor is user supplied; the interval has no automatic confidence-level guarantee. Balanced sinusoidal system.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `current` | RMS line current | 10 | A |
| `pf` | Displacement power factor (lagging) | 0.8 | pu |
| `u_voltage` | Voltage standard uncertainty | 1 | V |
| `u_current` | Current standard uncertainty | 0.1 | A |
| `u_pf` | Power factor standard uncertainty | 0.01 | pu |
| `coverage` | Coverage factor | 2 | pu |

## Derivation

1. `P = sqrt(3) V I pf`
2. `u_P² = (sqrt(3) I pf u_V)² + (sqrt(3) V pf u_I)² + (sqrt(3) V I u_pf)²`
3. `U = k u_P; interval = P +/- U`

## Reference outputs

- `power` = 5542.562584220407 W
- `standard_uncertainty` = 89.7997772825746 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate power_uncertainty --inputs '{"voltage": 400, "current": 10, "pf": 0.8, "u_voltage": 1, "u_current": 0.1, "u_pf": 0.01, "coverage": 2}'
python -m unittest tests.test_calc_power_uncertainty
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
