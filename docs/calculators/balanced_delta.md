# Balanced delta load

Category: Three phase. Calculator ID: `balanced_delta`.

Balanced delta impedance load. Line current magnitude differs from branch current.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `resistance` | Resistance | 1 | ohm |
| `reactance` | Reactance (+ inductive) | 1 | ohm |

## Derivation

1. `V_branch = V_LL`
2. `I_branch = V_LL / Z`
3. `|I_line| = sqrt(3) |I_branch|`
4. `S_total = 3 V_LL conjugate(I_branch)`

## Reference outputs

- `branch_current` = 282.842712474619 A
- `line_current` = 489.8979485566356 A
- `power` = 240000 W
- `reactive` = 240000 var

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate balanced_delta --inputs '{"voltage": 400, "resistance": 1, "reactance": 1}'
python -m unittest tests.test_calc_balanced_delta
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
