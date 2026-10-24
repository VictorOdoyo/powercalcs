# Load energy and utilization

Category: Studies. Calculator ID: `energy_consumption`.

Constant average utilization over the specified duration; no tariff or demand-charge model.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `duration` | Duration | 3600 | s |
| `utilization` | Average utilization | 0.75 | pu |

## Derivation

1. `P_average = P_rated utilization`
2. `E = P_average duration`
3. `E_kWh = E_J / 3.6e6`

## Reference outputs

- `energy` = 27000000 J
- `energy_kwh` = 7.5 kWh
- `average_power` = 7500 W

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate energy_consumption --inputs '{"power": 10000, "duration": 3600, "utilization": 0.75}'
python -m unittest tests.test_calc_energy_consumption
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
