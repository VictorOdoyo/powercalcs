# Balanced star load

Category: Three phase. Calculator ID: `balanced_star`.

Balanced star-connected impedance load; ABC ideal sinusoidal source.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `voltage` | Line-to-line RMS voltage | 400 | V |
| `resistance` | Resistance | 1 | ohm |
| `reactance` | Reactance (+ inductive) | 1 | ohm |

## Derivation

1. `V_phase = V_LL / sqrt(3)`
2. `I_L = V_phase / Z`
3. `S_total = 3 V_phase conjugate(I_L)`

## Reference outputs

- `phase_voltage` = 230.94010767585033 V
- `line_current` = 163.29931618554522 A
- `power` = 80000 W
- `reactive` = 80000 var

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate balanced_star --inputs '{"voltage": 400, "resistance": 1, "reactance": 1}'
python -m unittest tests.test_calc_balanced_star
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
