from functools import partial
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

    result.append(f"{' ' * INDENT_SIZE * (level - 1)}{'}'}")
    return "\n".join(result)


def _format_node(
    key: str,
    value: Any,
    sign: str,
    level: int,
) -> str:

    if isinstance(value, dict):
        value = _format_dict(values=value, level=level)

    prefix = f"{' ' * (INDENT_SIZE * level - 2)}{sign} "
    return f"{prefix}{key}: {value}"


def _format_dict(values: dict[str, Any], level: int) -> str:
    rows = ["{"]

    for key, value in sorted(values.items(), key=itemgetter(0)):
        rows.append(
            _format_node(
                key=key,
                value=value,
                sign=" ",
                level=level + 1,
            )
        )

    rows.append(f"{' ' * INDENT_SIZE * level}{'}'}")
    return "\n".join(rows)
