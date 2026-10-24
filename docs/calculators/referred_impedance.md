# Refer transformer impedance

Category: Transformers. Calculator ID: `referred_impedance`.

Ideal transformer winding voltage ratio; use winding phase voltage ratio for differing star/delta connections.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `resistance` | Resistance | 1 | ohm |
| `reactance` | Reactance (+ inductive) | 1 | ohm |
| `ratio` | Target/source winding voltage ratio | 10 | pu |

## Derivation

1. `Z_target = Z_source (V_target / V_source)²`

## Reference outputs

- `referred` = [100, 100] ohm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate referred_impedance --inputs '{"resistance": 1, "reactance": 1, "ratio": 10}'
python -m unittest tests.test_calc_referred_impedance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
