# Stored capacitor energy

Category: Capacitors. Calculator ID: `capacitor_energy`.

Voltage is instantaneous or DC, not RMS. Single ideal capacitor; dielectric losses omitted.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `capacitance` | Capacitance | 0.001 | F |
| `instant_voltage` | Instantaneous/DC voltage | 400 | V |

## Derivation

1. `E = (1/2) C v²`
2. `q = C v`

## Reference outputs

- `energy` = 80 J
- `charge` = 0.4 C

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate capacitor_energy --inputs '{"capacitance": 0.001, "instant_voltage": 400}'
python -m unittest tests.test_calc_capacitor_energy
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
