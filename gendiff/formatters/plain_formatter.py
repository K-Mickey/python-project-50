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


def format_plain(diff: list[DiffNode], parent_name: str = "") -> str:
    result = []

    for node in sorted(diff, key=attrgetter("key")):
        node_name = node.key if not parent_name else f"{parent_name}.{node.key}"

        match node:
            case Unchanged(_, _):
                pass

            case Nested(_, children):
                nested_diff = format_plain(diff=children, parent_name=node_name)
                if nested_diff:
                    result.append(nested_diff)

            case Added(_, value):
                action = f"added with value: {_to_string(value)}"
                result.append(_format_row(node_name=node_name, action=action))

            case Removed(_, _):
                action = "removed"
                result.append(_format_row(node_name=node_name, action=action))

            case Changed(_, old_value, new_value):
                previous = _to_string(old_value)
                current = _to_string(new_value)
                action = f"updated. From {previous} to {current}"
                result.append(_format_row(node_name=node_name, action=action))

            case _:
                raise ValueError(f"Unknown node type: {type(node)}")

    return "\n".join(result)


def _format_row(node_name: str, action: str) -> str:
    return f"Property '{node_name}' was {action}"


def _to_string(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)
