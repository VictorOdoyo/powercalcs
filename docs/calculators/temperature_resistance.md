# Resistance at temperature

Category: Cables. Calculator ID: `temperature_resistance`.

Linear resistance-temperature approximation; alpha is referenced to T_ref. No thermal equilibrium calculation.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `resistance` | Resistance | 1 | ohm |
| `alpha` | Temperature coefficient at reference | 0.00393 | 1/degC |
| `reference_temp` | Reference temperature | 20 | degC |
| `temperature` | Operating temperature | 70 | degC |

## Derivation

1. `R(T) = R_ref [1 + alpha_ref (T - T_ref)]`

## Reference outputs

- `resistance_hot` = 1.1965 ohm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate temperature_resistance --inputs '{"resistance": 1, "alpha": 0.00393, "reference_temp": 20, "temperature": 70}'
python -m unittest tests.test_calc_temperature_resistance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
