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


def _get_structure(diff: list[DiffNode]) -> list[Any]:
    result = []
    for node in sorted(diff, key=attrgetter("key")):
        match node:
            case Nested(key, children):
                nested_diff = _get_structure(children)
                row = {"type": "nested", "key": key, "children": nested_diff}

            case Added(key, value):
                row = {"type": "added", "key": key, "value": value}

            case Removed(key, value):
                row = {"type": "removed", "key": key, "value": value}

            case Changed(key, old_value, new_value):
                row = {
                    "type": "changed",
                    "key": key,
                    "old_value": old_value,
                    "new_value": new_value,
                }

            case Unchanged(key, value):
                row = {"type": "unchanged", "key": key, "value": value}

            case _:
                raise ValueError(f"Unknown node type: {type(node)}")

        result.append(row)

    return result
