# Motor synchronous speed

Category: Motors. Calculator ID: `synchronous_speed`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `frequency` | Frequency | 50 | Hz |
| `poles` | Pole count | 4 | count |

## Derivation

1. `n_sync (rpm) = 120 f / poles`

## Reference outputs

- `speed` = 1500 rpm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate synchronous_speed --inputs '{"frequency": 50, "poles": 4}'
python -m unittest tests.test_calc_synchronous_speed
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
