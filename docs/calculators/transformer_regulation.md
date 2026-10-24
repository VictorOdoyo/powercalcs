# Approximate transformer regulation

Category: Transformers. Calculator ID: `transformer_regulation`.

First-order lagging-load regulation estimate on a consistent transformer base. Magnetizing branch omitted.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `resistance_pu` | Resistance | 0.01 | pu |
| `reactance_pu` | Reactance | 0.04 | pu |
| `pf` | Displacement power factor (lagging) | 0.8 | pu |
| `loading` | Load fraction | 1 | pu |

## Derivation

1. `regulation (%) approximately 100 loading (R_pu pf + X_pu sin(phi))`

## Reference outputs

- `regulation_percent` = 3.2 %

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate transformer_regulation --inputs '{"resistance_pu": 0.01, "reactance_pu": 0.04, "pf": 0.8, "loading": 1}'
python -m unittest tests.test_calc_transformer_regulation
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
