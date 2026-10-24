# Three-phase per-unit bases

Category: Transformers. Calculator ID: `three_phase_bases`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `apparent` | Three-phase base power | 100000 | VA |

## Derivation

1. `I_base = S_3phase / (sqrt(3) V_LL)`
2. `Z_base = V_LL² / S_3phase`
3. `V_phase_base = V_LL / sqrt(3)`

## Reference outputs

- `base_current` = 144.33756729740645 A
- `base_impedance` = 1.6 ohm
- `phase_voltage` = 230.94010767585033 V

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate three_phase_bases --inputs '{"voltage": 400, "apparent": 100000}'
python -m unittest tests.test_calc_three_phase_bases
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
