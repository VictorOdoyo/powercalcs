# Sequence voltage unbalance

Category: Phasors. Calculator ID: `voltage_unbalance`.

Sequence-based voltage unbalance factor; input sequence magnitudes must come from a consistent phasor measurement.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `positive` | Positive-sequence magnitude | 230 | V |
| `negative` | Negative-sequence magnitude | 4.6 | V |

## Derivation

1. `VUF (%) = 100 |V2| / |V1|`

## Reference outputs

- `unbalance_percent` = 2 %

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate voltage_unbalance --inputs '{"positive": 230, "negative": 4.6}'
python -m unittest tests.test_calc_voltage_unbalance
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
