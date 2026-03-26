from operator import attrgetter, itemgetter
from typing import Any

from gendiff.diff_builder import (
    Added,
    Changed,
    DiffNode,
    Nested,
    Removed,
    Unchanged,
)

INDENT = 4


def format_stylish(
    diff: list[DiffNode],
    level: int = 1,
) -> str:
    result = ["{"]

    for node in sorted(diff, key=attrgetter("key")):
        match node:
            case Nested(key, children):
                nested_diff = format_stylish(children, level + 1)
                params = [(key, nested_diff, " ")]
            case Added(key, value):
                params = [(key, value, "+")]
            case Removed(key, value):
                params = [(key, value, "-")]
            case Changed(key, old_value, new_value):
                params = [(key, old_value, "-"), (key, new_value, "+")]
            case Unchanged(key, value):
                params = [(key, value, " ")]
            case _:
                raise ValueError(f"Unknown node type: {type(node)}")

        result += [
            _format_row(key=key, value=value, sign=sign, level=level)
            for key, value, sign in params
        ]

    result += [f"{' ' * _get_indent(level - 1)}{'}'}"]
    return "\n".join(result)


def _format_row(
    key: str,
    value: Any,
    sign: str,
    level: int,
) -> str:

    if isinstance(value, dict):
        dict_values = ["{"]
        dict_values += [
            _format_row(key, value, " ", level + 1)
            for key, value in sorted(value.items(), key=itemgetter(0))
        ]

        dict_values += [f"{' ' * INDENT * level}{'}'}"]
        value = "\n".join(dict_values)

    prefix = f"{' ' * (_get_indent(level) - 2)}{sign} "
    return f"{prefix}{key}: {value}"


def _get_indent(level: int) -> int:
    return INDENT * level
