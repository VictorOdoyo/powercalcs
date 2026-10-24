"""Shared result contract, input validation, and calculation provenance."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import math
from .units import convert

@dataclass(frozen=True)
class Field:
    key: str
    label: str
    unit: str
    dimension: str
    default: float
    minimum: float | None = None
    maximum: float | None = None
    exclusive_minimum: bool = False
    integer: bool = False

    def parse(self, raw):
        if isinstance(raw, dict):
            if set(raw) != {'value', 'unit'}:
                raise ValueError(f'{self.label}: quantity needs value and unit')
            value = convert(raw['value'], raw['unit'], self.dimension)
        else:
            value = convert(raw, self.unit, self.dimension)
        if self.minimum is not None and (value < self.minimum or (self.exclusive_minimum and value == self.minimum)):
            raise ValueError(f'{self.label}: must be {">" if self.exclusive_minimum else ">="} {self.minimum} {self.unit}')
        if self.maximum is not None and value > self.maximum:
            raise ValueError(f'{self.label}: must be <= {self.maximum} {self.unit}')
        if self.integer and not value.is_integer():
            raise ValueError(f'{self.label}: must be an integer')
        return value

def finite(value):
    if isinstance(value, complex):
        return math.isfinite(value.real) and math.isfinite(value.imag)
    return math.isfinite(value)

def encode(value):
    if isinstance(value, complex):
        return {'real': value.real, 'imag': value.imag, 'magnitude': abs(value),
                'angle_deg': math.degrees(math.atan2(value.imag, value.real))}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value

@dataclass(frozen=True)
class Calculator:
    id: str
    title: str
    category: str
    description: str
    fields: tuple
    outputs: dict
    formulas: tuple
    assumptions: tuple
    compute: object

    def metadata(self):
        return {'id': self.id, 'title': self.title, 'category': self.category,
                'description': self.description, 'fields': [asdict(f) for f in self.fields],
                'outputs': self.outputs, 'formulas': self.formulas, 'assumptions': self.assumptions}

    def run(self, inputs):
        if not isinstance(inputs, dict):
            raise ValueError('Inputs must be an object')
        unknown = set(inputs) - {f.key for f in self.fields}
        if unknown:
            raise ValueError('Unknown inputs: ' + ', '.join(sorted(unknown)))
        missing = [f.key for f in self.fields if f.key not in inputs]
        if missing:
            raise ValueError('Missing inputs: ' + ', '.join(missing))
        values = {f.key: f.parse(inputs[f.key]) for f in self.fields}
        try:
            results = self.compute(**values)
        except (ArithmeticError, ValueError) as exc:
            raise ValueError(f'Calculation domain error: {exc}') from exc
        if set(results) != set(self.outputs) or not all(finite(v) for v in results.values()):
            raise ValueError('Calculation produced undefined or out-of-range results')
        return {'calculator': self.id, 'title': self.title, 'version': '1.0.0',
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'inputs_si': values, 'input_units': {f.key: f.unit for f in self.fields},
                'results': encode(results), 'output_units': self.outputs,
                'steps': [{'number': i + 1, 'equation': equation} for i, equation in enumerate(self.formulas)],
                'assumptions': list(self.assumptions)}
