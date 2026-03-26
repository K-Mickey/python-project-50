from enum import StrEnum
from pathlib import Path

from gendiff.diff_builder import get_diff
from gendiff.file_parser import parse
from gendiff.json_formatter import format_stylish


class FormatName(StrEnum):
    STYLISH = "stylish"


def generate_diff(
    file_path1: Path,
    file_path2: Path,
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
        case _:
            raise ValueError(f"Unknown format: {format_name}")
