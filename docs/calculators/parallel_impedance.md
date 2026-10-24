# Parallel complex impedances

Category: Impedance. Calculator ID: `parallel_impedance`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `r1` | Branch 1 resistance | 10 | ohm |
| `x1` | Branch 1 reactance | 10 | ohm |
| `r2` | Branch 2 resistance | 10 | ohm |
| `x2` | Branch 2 reactance | 10 | ohm |

## Derivation

1. `Z_eq = Z1 Z2 / (Z1 + Z2)`

## Reference outputs

- `equivalent` = [5, 5] ohm

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate parallel_impedance --inputs '{"r1": 10, "x1": 10, "r2": 10, "x2": 10}'
python -m unittest tests.test_calc_parallel_impedance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
