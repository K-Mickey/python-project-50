from functools import partial
from operator import attrgetter
from typing import Any

from gendiff.diff_builder import (
    Added,
    Changed,
    DiffNode,
    Nested,
    Removed,
    Unchanged,
)

INDENT_SIZE = 4


def format_stylish(
    diff: list[DiffNode],
    level: int = 1,
) -> str:
    result = ["{"]

    for node in sorted(diff, key=attrgetter("key")):
        format_node = partial(_format_node, key=node.key, level=level)
        match node:
            case Nested(_, children):
                nested_diff = format_stylish(children, level + 1)
                result.append(format_node(value=nested_diff, sign=" "))
            case Added(_, value):
                result.append(format_node(value=value, sign="+"))
            case Removed(_, value):
                result.append(format_node(value=value, sign="-"))
            case Changed(_, old_value, new_value):
                result.append(format_node(value=old_value, sign="-"))
                result.append(format_node(value=new_value, sign="+"))
            case Unchanged(_, value):
                result.append(format_node(value=value, sign=" "))
            case _:
                raise ValueError(f"Unknown node type: {type(node)}")

    prev_level = level - 1
    result.append(f"{_indent(prev_level)}{'}'}")
    return "\n".join(result)


def _format_node(
    key: str,
    value: Any,
    sign: str,
    level: int,
) -> str:

    if isinstance(value, dict):
        value = _format_dict(values=value, level=level)

    prefix = _indent(level=level, sign=sign)
    return f"{prefix}{key}: {_to_str(value)}"


def _format_dict(values: dict[str, Any], level: int) -> str:
    rows = ["{"]

    for key, value in sorted(values.items()):
        rows.append(
            _format_node(
                key=key,
                value=value,
                sign=" ",
                level=level + 1,
            )
        )

    rows.append(f"{_indent(level)}{'}'}")
    return "\n".join(rows)


def _indent(level: int, sign: str = "") -> str:
    base_indent = INDENT_SIZE * level

    if sign:
        sign_space = 2
        return f"{' ' * (base_indent - sign_space)}{sign} "
    return " " * base_indent


def _to_str(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    return str(value)
