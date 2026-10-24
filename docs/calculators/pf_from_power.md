# Power factor from P and S

Category: Power. Calculator ID: `pf_from_power`.

Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `apparent` | Apparent power | 12500 | VA |

## Derivation

1. `pf = P / S`
2. `Q = sqrt(S² - P²)`

## Reference outputs

- `pf` = 0.8 pu
- `reactive` = 7500 var

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate pf_from_power --inputs '{"power": 10000, "apparent": 12500}'
python -m unittest tests.test_calc_pf_from_power
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
