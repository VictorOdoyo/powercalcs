# Impedance to per unit

Category: Transformers. Calculator ID: `impedance_per_unit`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `resistance` | Resistance | 1 | ohm |
| `reactance` | Reactance (+ inductive) | 1 | ohm |
| `base_impedance` | Base impedance | 10 | ohm |

## Derivation

1. `Z_pu = Z_ohm / Z_base`

## Reference outputs

- `impedance_pu` = [0.1, 0.1] pu

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate impedance_per_unit --inputs '{"resistance": 1, "reactance": 1, "base_impedance": 10}'
python -m unittest tests.test_calc_impedance_per_unit
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
