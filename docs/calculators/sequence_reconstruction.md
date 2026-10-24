# Reconstruct phase phasors

Category: Phasors. Calculator ID: `sequence_reconstruction`.

ABC positive sequence; a = exp(j 120 degrees).

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `zero_mag` | zero magnitude | 10 | V |
| `zero_angle` | zero angle | 0 | deg |
| `positive_mag` | positive magnitude | 230 | V |
| `positive_angle` | positive angle | 0 | deg |
| `negative_mag` | negative magnitude | 0 | V |
| `negative_angle` | negative angle | 0 | deg |

## Derivation

1. `VA = V0 + V1 + V2`
2. `VB = V0 + a² V1 + a V2`
3. `VC = V0 + a V1 + a² V2`

## Reference outputs

- `va` = [240, 0] V
- `vb` = [-105, -199.18584287042088] V
- `vc` = [-105, 199.18584287042088] V

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate sequence_reconstruction --inputs '{"zero_mag": 10, "zero_angle": 0, "positive_mag": 230, "positive_angle": 0, "negative_mag": 0, "negative_angle": 0}'
python -m unittest tests.test_calc_sequence_reconstruction
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
