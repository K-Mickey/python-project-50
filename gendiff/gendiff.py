from enum import StrEnum
from pathlib import Path

from gendiff.diff_builder import get_diff
from gendiff.file_parser import parse
from gendiff.formatters import format_json, format_plain, format_stylish


class FormatName(StrEnum):
    STYLISH = "stylish"
    PLAIN = "plain"
    JSON = "json"


def generate_diff(
    file_path1: Path | str,
    file_path2: Path | str,
    format_name: str = FormatName.STYLISH,
) -> str:

    file1 = parse(file_path1)
    file2 = parse(file_path2)

    diff = get_diff(
        old_dict=file1,
        new_dict=file2,
    )

    match format_name:
        case FormatName.STYLISH:
            return format_stylish(diff)
        case FormatName.PLAIN:
            return format_plain(diff)
        case FormatName.JSON:
            return format_json(diff)
        case _:
            raise ValueError(f"Unknown format: {format_name}")
