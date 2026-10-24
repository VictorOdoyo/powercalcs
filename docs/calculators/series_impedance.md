# Series impedance

Category: Impedance. Calculator ID: `series_impedance`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `resistance` | Resistance | 1 | ohm |
| `reactance` | Reactance (+ inductive) | 1 | ohm |

## Derivation

1. `Z = R + jX`
2. `|Z| = sqrt(R² + X²)`
3. `angle(Z) = atan2(X,R)`

## Reference outputs

- `impedance` = [1, 1] ohm
- `magnitude` = 1.4142135623730951 ohm
- `angle` = 45 deg

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate series_impedance --inputs '{"resistance": 1, "reactance": 1}'
python -m unittest tests.test_calc_series_impedance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
