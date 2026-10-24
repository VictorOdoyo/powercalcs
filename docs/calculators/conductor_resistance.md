# Resistance from geometry

Category: Cables. Calculator ID: `conductor_resistance`.

Uniform conductor and specified material temperature. DC resistance; skin and proximity effects omitted.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `resistivity` | Material resistivity | 1.724e-08 | ohm*m |
| `length` | Conductor length | 100 | m |
| `area` | Cross-sectional area | 2.5e-05 | m2 |

## Derivation

1. `R = rho L / A`

## Reference outputs

- `resistance` = 0.06896 ohm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate conductor_resistance --inputs '{"resistivity": 1.724e-08, "length": 100, "area": 2.5e-05}'
python -m unittest tests.test_calc_conductor_resistance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
