# Capacitive reactance

Category: Impedance. Calculator ID: `capacitive_reactance`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `frequency` | Frequency | 50 | Hz |
| `capacitance` | Capacitance | 0.0001 | F |

## Derivation

1. `X_C = -1 / (2 pi f C)`

## Reference outputs

- `reactance` = -31.830988618379067 ohm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate capacitive_reactance --inputs '{"frequency": 50, "capacitance": 0.0001}'
python -m unittest tests.test_calc_capacitive_reactance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
