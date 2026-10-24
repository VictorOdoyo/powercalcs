# Ideal transformer turns ratio

Category: Transformers. Calculator ID: `turns_ratio`.

Ideal transformer; voltages and currents are winding quantities, not necessarily line quantities.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `primary` | Primary winding RMS voltage | 11000 | V |
| `secondary` | Secondary winding RMS voltage | 230 | V |
| `secondary_current` | Secondary winding current | 100 | A |

## Derivation

1. `a = V_primary / V_secondary = N_primary / N_secondary`
2. `I_primary = I_secondary / a`

## Reference outputs

- `ratio` = 47.82608695652174 pu
- `primary_current` = 2.090909090909091 A

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate turns_ratio --inputs '{"primary": 11000, "secondary": 230, "secondary_current": 100}'
python -m unittest tests.test_calc_turns_ratio
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
