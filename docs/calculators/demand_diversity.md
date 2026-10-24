# Demand and diversity factors

Category: Studies. Calculator ID: `demand_diversity`.

All demands use the same averaging interval and active-power basis. Connected loads are upper bounds for individual maximum demand.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `connected` | Total connected load | 100000 | W |
| `maximum` | Coincident maximum demand | 60000 | W |
| `individual_sum` | Sum of individual maximum demands | 90000 | W |

## Derivation

1. `Demand factor = coincident maximum / connected load`
2. `Diversity factor = sum(individual maxima) / coincident maximum`
3. `Coincidence factor = coincident maximum / sum(individual maxima)`

## Reference outputs

- `demand_factor` = 0.6 pu
- `diversity_factor` = 1.5 pu
- `coincidence_factor` = 0.6666666666666666 pu

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate demand_diversity --inputs '{"connected": 100000, "maximum": 60000, "individual_sum": 90000}'
python -m unittest tests.test_calc_demand_diversity
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
