# Mechanical shaft torque

Category: Motors. Calculator ID: `shaft_torque`.

Steady mechanical shaft power and nonzero rotational speed; no transient inertial torque.

## Inputs and worked example

Bare numbers use the displayed units below. Quantity objects may use another compatible unit, e.g. `{"value": 0.4, "unit": "kV"}`. The engine converts values to SI before evaluating the equations.

| Key | Meaning | Example | Unit |
| --- | --- | --- | --- |
| `power` | Active power | 10000 | W |
| `speed` | Shaft speed | 1500 | rpm |

## Derivation

1. `omega = 2 pi n / 60`
2. `T = P_shaft / omega`

## Reference outputs

- `torque` = 63.66197723675814 Nm
- `angular_speed` = 157.07963267948966 rad/s

Complex reference values are `[real, imaginary]`; API outputs also include magnitude and angle in degrees. Numerical results use double precision; display rounding does not change the exported values.

## Reproduce

```sh
python -m powercalcs calculate shaft_torque --inputs '{"power": 10000, "speed": 1500}'
python -m unittest tests.test_calc_shaft_torque
```

These reference outputs are analytical checks, not experimental certification. See [model scope](../MODELS.md) for conventions and applicability.
