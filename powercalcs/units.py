"""Dimension-tagged conversions; field values are normalized to SI."""
import math
from importlib import import_module
from pathlib import Path

def catalog():
    entries = {}
    for path in sorted((Path(__file__).parent / 'unit_definitions').glob('u_*.py')):
        entries.update(import_module('powercalcs.unit_definitions.' + path.stem).UNITS)
    return entries

def convert(value, source, dimension):
    if not isinstance(source, str):
        raise ValueError('Unit must be a string')
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Quantity must be a finite number')
    try:
        actual, scale = catalog()[source]
    except KeyError as exc:
        raise ValueError(f'Unknown unit: {source}') from exc
    if actual != dimension:
        raise ValueError(f'{source} has dimension {actual}; expected {dimension}')
    result = value * scale
    if not math.isfinite(result):
        raise ValueError('Converted quantity exceeds numerical range')
    return result
