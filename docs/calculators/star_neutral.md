# Unbalanced star with neutral

Category: Three phase. Calculator ID: `star_neutral`.

Ideal zero-impedance neutral fixes the load star point. Phase currents flow source to load; neutral return flows load to source.

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

1. `V_A,V_B,V_C = (V_LL/sqrt(3)) at 0,-120,+120 degrees`
2. `I_k = V_k / Z_k`
3. `I_neutral_return = I_A + I_B + I_C`
4. `S_total = sum(V_k conjugate(I_k))`

## Reference outputs

- `ia` = [23.094010767585033, 0] A
- `neutral_return` = [11.54700538379252, 0] A
- `power` = 10666.666666666668 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate star_neutral --inputs '{"voltage": 400, "ra": 10, "xa": 0, "rb": 20, "xb": 0, "rc": 20, "xc": 0}'
python -m unittest tests.test_calc_star_neutral
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
