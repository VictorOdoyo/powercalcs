# Unbalanced delta currents

Category: Three phase. Calculator ID: `delta_unbalanced`.

Inputs labelled phase A/B/C represent delta branches AB/BC/CA respectively. Branch directions AB, BC, CA; ideal ABC source.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `ra` | Phase A resistance | 10 | ohm |
| `xa` | Phase A reactance | 0 | ohm |
| `rb` | Phase B resistance | 20 | ohm |
| `xb` | Phase B reactance | 0 | ohm |
| `rc` | Phase C resistance | 20 | ohm |
| `xc` | Phase C reactance | 0 | ohm |

## Derivation

1. `I_AB = (V_A - V_B) / Z_AB; similarly BC and CA`
2. `I_A = I_AB - I_CA; I_B = I_BC - I_AB; I_C = I_CA - I_BC`
3. `P = real(sum(V_branch conjugate(I_branch)))`

## Reference outputs

- `iab` = [34.64101615137754, 20] A
- `ia` = [51.96152422706631, 10] A
- `power` = 32000 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate delta_unbalanced --inputs '{"voltage": 400, "ra": 10, "xa": 0, "rb": 20, "xb": 0, "rc": 20, "xc": 0}'
python -m unittest tests.test_calc_delta_unbalanced
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
