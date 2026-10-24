# Contributing

Use Python 3.11 or newer. The runtime has no third-party dependencies. Run `python -m unittest discover -s tests -v` before opening a pull request.

For a new model:

1. Define the engineering question, sign conventions, applicability limits and authoritative formula source.
2. Add `powercalcs/calculators/c_<id>.py` with a `Calculator` specification and pure compute function. All inputs must have dimensions and appropriate domain bounds. Do not infer missing electrical quantities silently.
3. Write an independently calculated reference case. Include a limiting case or physical invariant for nontrivial circuit behavior; avoid deriving expected values by calling the implementation under test.
4. Add `docs/calculators/<id>.md` with a worked example, equations, units and assumptions.
5. Check the model in the browser, including units, errors, exported JSON and printed output. Update catalog-count assertions if intentionally adding a calculator.

For unit conversions, define factors to the dimension's base unit and verify compatible/incompatible dimensions. Offset temperature conversions require a separate design, not a scale-factor shortcut.

Keep commits focused on a reviewable change. Implementation, independent validation, and engineering documentation may be separate commits. Never add empty commits or manipulate authorship dates to manufacture project history.
