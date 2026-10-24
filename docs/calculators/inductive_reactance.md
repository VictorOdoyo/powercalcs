# Inductive reactance

Category: Impedance. Calculator ID: `inductive_reactance`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `frequency` | Frequency | 50 | Hz |
| `inductance` | Inductance | 0.01 | H |

## Derivation

1. `X_L = 2 pi f L`

## Reference outputs

- `reactance` = 3.141592653589793 ohm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate inductive_reactance --inputs '{"frequency": 50, "inductance": 0.01}'
python -m unittest tests.test_calc_inductive_reactance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
