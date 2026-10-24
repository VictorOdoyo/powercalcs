# Power-factor phase angle

Category: Power. Calculator ID: `phase_angle`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `pf` | Displacement power factor (lagging) | 0.8 | pu |

## Derivation

1. `phi = acos(pf)`
2. `tan(phi) = sqrt(1 - pf²) / pf`

## Reference outputs

- `angle` = 36.86989764584401 deg
- `tan_phi` = 0.75 pu

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate phase_angle --inputs '{"pf": 0.8}'
python -m unittest tests.test_calc_phase_angle
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
