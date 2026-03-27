import json
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

INDENT_SIZE = 2


def format_json(diff: list[DiffNode]) -> str:
    structured_diff = _get_structure(diff)
    return json.dumps(structured_diff, indent=INDENT_SIZE)


def _get_structure(diff: list[DiffNode]) -> list[dict[str, Any]]:
    result = []
    for node in sorted(diff, key=attrgetter("key")):
        match node:
            case Nested(key, children):
                nested_diff = _get_structure(children)
                node_dict = {
                    "type": "nested",
                    "key": key,
                    "children": nested_diff,
                }

            case Added(key, value):
                node_dict = {"type": "added", "key": key, "value": value}

            case Removed(key, value):
                node_dict = {"type": "removed", "key": key, "value": value}

            case Changed(key, old_value, new_value):
                node_dict = {
                    "type": "changed",
                    "key": key,
                    "old_value": old_value,
                    "new_value": new_value,
                }

            case Unchanged(key, value):
                node_dict = {"type": "unchanged", "key": key, "value": value}

            case _:
                raise ValueError(f"Unknown node type: {type(node)}")

        result.append(node_dict)

    return result
