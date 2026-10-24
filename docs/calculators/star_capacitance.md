# Star capacitor-bank sizing

Category: Capacitors. Calculator ID: `star_capacitance`.

Balanced ideal three-phase bank. Output is the capacitance of each star leg or delta branch, not the total capacitance.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `frequency` | Frequency | 50 | Hz |
| `rating` | Total bank reactive rating | 50000 | var |

## Derivation

1. `C_per_phase = Q_bank / (1 omega V_LL²)`
2. `omega = 2 pi f`

## Reference outputs

- `capacitance_per_phase` = 0.000994718394324346 F

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate star_capacitance --inputs '{"voltage": 400, "frequency": 50, "rating": 50000}'
python -m unittest tests.test_calc_star_capacitance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
