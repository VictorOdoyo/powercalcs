# Unbalanced star with floating neutral

Category: Three phase. Calculator ID: `star_floating`.

Three-wire star load with no neutral connection. Ideal balanced ABC source; no earth shunts.

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

1. `Y_k = 1 / Z_k`
2. `V_n = sum(V_k Y_k) / sum(Y_k)`
3. `I_k = (V_k - V_n) Y_k`
4. `P = real(sum((V_k - V_n) conjugate(I_k)))`

## Reference outputs

- `neutral_displacement` = [57.735026918962596, 0] V
- `ia` = [17.320508075688775, 0] A
- `power` = 10000 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate star_floating --inputs '{"voltage": 400, "ra": 10, "xa": 0, "rb": 20, "xb": 0, "rc": 20, "xc": 0}'
python -m unittest tests.test_calc_star_floating
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
