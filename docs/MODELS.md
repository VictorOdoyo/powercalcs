# Engineering conventions and model boundaries

## Phasors and power

All AC magnitudes are RMS unless explicitly marked instantaneous/DC. The time convention is `exp(j omega t)`. ABC positive-sequence phase angles are 0, -120, +120 degrees. Complex power is `S = V conjugate(I)`. Positive reactive power is inductive consumption. Balanced three-phase power uses line-to-line voltage and line current; total three-phase apparent power is used for per-unit bases.

Power-factor-only calculators use nonnegative displacement power factor with a **lagging** assumption. They do not model waveform distortion or true power factor with harmonics. Impedance-based calculators accept signed reactance and therefore can represent capacitive loads directly. Exported complex quantities contain real/imaginary parts, magnitude, and angle in degrees.

## Unbalanced circuits

The solid-neutral star model uses an ideal zero-impedance neutral. Neutral return current flows load to source, so `I_N = I_A + I_B + I_C`. The floating-star model solves the load star potential from its phase admittances, with no ground path. Delta branch labels are AB, BC, CA; line currents follow Kirchhoff's current law. The source is ideal and balanced in these load models. Source asymmetry is supported in the separate symmetrical-component calculator, not in the star/delta source models.

## Approximate models

Cable voltage drop uses a first-order longitudinal approximation. It does not solve the full receiving-end phasor or a voltage-dependent load. Supply voltage is used as the percentage denominator. Cable R and X are per conductor; length is one-way. Transformer regulation is first order. Transformer-limited fault current assumes an infinite upstream source, no motor contribution, no voltage factor and no DC offset. It is not an IEC/ANSI short-circuit implementation. Starting voltage drop fixes starting current and does not model acceleration or voltage feedback. Large predicted drops are evidence that the approximation is outside a useful planning range; they are not a solved motor terminal voltage.

Resistance from geometry is DC resistance. Temperature correction is a linear model, not an ampacity/thermal solver. Parallel feeders have no mutual impedance. Capacitor models omit harmonics, tolerance, switching transients, detuning reactors and discharge circuits. Motor efficiency models are motoring models; signed slip separately permits supersynchronous operation. No calculator selects protective devices or certifies an installation design.

## Units and numerical behavior

Each input carries a semantic dimension. Active, reactive and apparent power remain distinct even though their physical dimensions match. Degree inputs are converted to radians for computation; input provenance reports radians. Other numerical base units are V, A, W, var, VA, ohm, H, F, Hz, m, m², s, J, and the explicitly defined practical speed base rpm. Percent fields normalize to a fraction; percent *outputs* are scaled by 100 and tagged `%`. Celsius is supported only as an explicitly named temperature coordinate; there are no Kelvin/Fahrenheit offset conversions.

Python double precision is used. Invalid bounds, nonfinite quantities, zero divisors and undefined results are rejected. Very ill-conditioned complex circuits can still lose precision; this is not an interval-arithmetic solver. Display rounding affects only the UI. Underflow to zero is possible at extreme scales. Integer pole/conductor counts are enforced. Near-zero phasor angles have little physical meaning.

## Uncertainty

The dedicated three-phase power uncertainty model uses first-order root-sum-square propagation for independent voltage, current and power-factor standard uncertainties. Its interval is `P +/- k u_P` with a user-specified coverage factor. It is not a guaranteed worst-case bound or a claimed confidence interval. Correlation, input distributions, nonlinear behavior and unit-factor uncertainty are omitted. Other calculators report deterministic results and do not implicitly claim uncertainty bounds.

## Derivations and traceability

Each result provides the model equations in evaluation order, normalized inputs with units, output units, model assumptions, package version and UTC timestamp. The inputs and results together let a reader substitute the values into the equations. Individual intermediate quantities are returned where useful (e.g. apparent power, phase voltage, initial/target var and base quantities). No standard-compliance claim is implied by a worked derivation.

## References

- Schneider Electric, [Calculation of voltage drop in steady load conditions](https://www.electrical-installation.org/enwiki/Calculation_of_voltage_drop_in_steady_load_conditions): longitudinal single/three-phase voltage-drop equations and input conventions.
- Schneider Electric, [Theoretical principles to improve power factor](https://www.electrical-installation.org/enwiki/Theoretical_principles_to_improve_power_factor): reactive-power compensation relationships.
- NPTEL, IIT Kharagpur, [Electrical Machines II course scope](https://archive.nptel.ac.in/content/syllabus_pdf/108105017.pdf): synchronous speed, slip and induction-machine power relationships; this course outline is a study reference, not a numerical benchmark.

Formula implementations and examples are original code and documentation. Reference cases are hand-specified analytical calculations; there has been no comparison to laboratory measurements or a commercial certified design package.
