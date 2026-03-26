from typing import Any, NamedTuple


class Nested(NamedTuple):
    key: str
    children: list["DiffNode"]


class Added(NamedTuple):
    key: str
    value: Any


class Removed(NamedTuple):
    key: str
    value: Any


class Unchanged(NamedTuple):
    key: str
    value: Any


class Changed(NamedTuple):
    key: str
    old_value: Any
    new_value: Any


DiffNode = Nested | Added | Removed | Unchanged | Changed


def get_diff(
    old_dict: dict[str, Any],
    new_dict: dict[str, Any],
) -> list[DiffNode]:

    added_keys = new_dict.keys() - old_dict.keys()
    diff = [Added(key, new_dict[key]) for key in added_keys]

    removed_keys = old_dict.keys() - new_dict.keys()
    diff += [Removed(key, old_dict[key]) for key in removed_keys]

    for key in old_dict.keys() & new_dict.keys():
        old_value = old_dict.get(key)
        new_value = new_dict.get(key)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            nested_diff = get_diff(old_value, new_value)
            diff += [Nested(key, nested_diff)]
        elif old_value != new_value:
            diff += [Changed(key, old_value, new_value)]
        else:
            diff += [Unchanged(key, old_value)]

    return diff
