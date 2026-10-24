# Ideal LC resonance

Category: Impedance. Calculator ID: `resonant_frequency`.

Ideal lumped LC circuit; parasitic losses, source impedance, and distributed effects omitted.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `inductance` | Inductance | 0.01 | H |
| `capacitance` | Capacitance | 0.0001 | F |

## Derivation

1. `f0 = 1 / (2 pi sqrt(L C))`

## Reference outputs

- `frequency` = 159.15494309189535 Hz

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate resonant_frequency --inputs '{"inductance": 0.01, "capacitance": 0.0001}'
python -m unittest tests.test_calc_resonant_frequency
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
