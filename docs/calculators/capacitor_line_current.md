# Three-phase capacitor line current

Category: Capacitors. Calculator ID: `capacitor_line_current`.

Balanced sinusoidal ideal capacitor bank. Excludes harmonic current and manufacturing tolerance.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `rating` | Total bank reactive power | 50000 | var |

## Derivation

1. `I_line = Q_bank / (sqrt(3) V_LL)`

## Reference outputs

- `line_current` = 72.16878364870323 A

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate capacitor_line_current --inputs '{"voltage": 400, "rating": 50000}'
python -m unittest tests.test_calc_capacitor_line_current
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
