# API contract

`GET /api/catalog` returns `calculators`, `units` and `version`. Each calculator declares ID, title, category, description, fields, outputs, formulas and assumptions. Each field declares its key, label, default unit, semantic dimension, example value and bounds. Defaults are for UI examples; the calculation API requires every input explicitly.

`POST /api/calculate` accepts `application/json` with exactly `calculator` and `inputs`. Inputs must be an object with the declared keys. Values are either finite JSON numbers or `{ "value": 1, "unit": "kV" }`. Booleans, numeric strings, incompatible units, unknown fields and missing fields are rejected.

Successful response fields:

| Field | Meaning |
| --- | --- |
| calculator, title | Model identity |
| version | Implementation version |
| timestamp | Evaluation time, UTC ISO 8601 |
| inputs_si | Normalized values; angles in radians, speed in rpm |
| input_units | Units of the normalized values |
| results | Scalar values or complex phasor records |
| output_units | Unit for each output key |
| steps | Ordered equations used by the model |
| assumptions | Applicable model conditions |

Complex records use `real`, `imag`, `magnitude` and `angle_deg`. Errors use `{ "error": "message" }` with HTTP 400 for invalid calculations, 403 for cross-origin submissions, 404 for unknown paths, 413 for absent/oversized bodies and 415 for incorrect content type. The server is a loopback-only standard-library adapter intended for a local trusted machine.

The Python interface is `powercalcs.catalog.calculate(id, inputs)`. It returns the same successful record and raises `ValueError` on invalid input. `calculators()` supplies the registered specifications. Do not mutate the returned catalog or calculator metadata.
