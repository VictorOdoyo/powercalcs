# Conductor I²R losses

Category: Cables. Calculator ID: `conductor_losses`.

Equal RMS current and end-to-end resistance in every counted conductor. Neutral losses must be evaluated separately if unequal.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `current` | RMS line current | 10 | A |
| `resistance` | Resistance | 1 | ohm |
| `conductors` | Loaded conductor count | 3 | count |

## Derivation

1. `P_loss = n I² R`

## Reference outputs

- `loss` = 300 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate conductor_losses --inputs '{"current": 10, "resistance": 1, "conductors": 3}'
python -m unittest tests.test_calc_conductor_losses
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
