# Transformer-limited three-phase fault

Category: Transformers. Calculator ID: `transformer_fault`.

Simplified symmetrical RMS bolted fault estimate with an infinite upstream source. Excludes source/cable impedance, voltage factors, motor contribution, and DC offset; not a standard-compliant fault study.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `apparent` | Transformer rating | 100000 | VA |
| `impedance_pu` | Transformer impedance magnitude | 0.05 | pu |

## Derivation

1. `I_rated = S / (sqrt(3) V_LL)`
2. `I_fault approximately I_rated / |Z_pu|`

## Reference outputs

- `rated_current` = 144.33756729740645 A
- `fault_current` = 2886.751345948129 A

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate transformer_fault --inputs '{"voltage": 400, "apparent": 100000, "impedance_pu": 0.05}'
python -m unittest tests.test_calc_transformer_fault
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
