# Power-factor correction rating

Category: Capacitors. Calculator ID: `pf_correction`.

Sinusoidal lagging load with constant active power. Correction to a lagging target only; harmonic resonance and switching duties require a separate study.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `initial_pf` | Initial lagging power factor | 0.8 | pu |
| `target_pf` | Target lagging power factor | 0.95 | pu |

## Derivation

1. `Q_initial = P tan(acos(pf_initial))`
2. `Q_target = P tan(acos(pf_target))`
3. `Q_capacitor = Q_initial - Q_target`

## Reference outputs

- `required_var` = 4213.158948211368 var
- `initial_var` = 7500 var
- `target_var` = 3286.841051788632 var

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate pf_correction --inputs '{"power": 10000, "initial_pf": 0.8, "target_pf": 0.95}'
python -m unittest tests.test_calc_pf_correction
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
