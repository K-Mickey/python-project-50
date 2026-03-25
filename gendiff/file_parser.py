import json
from pathlib import Path

import yaml

FILE_ENCODING = "utf-8"


class UnsupportedFileFormat(ValueError):
    def __init__(self, suffix):
        super().__init__(f"Unsupported file format: {suffix}")


def parse(file_path: Path) -> dict:
    file = file_path.read_text(encoding=FILE_ENCODING)
    return choose_parser(file_path, file)


def choose_parser(file_path: Path, file: str) -> dict:
    match file_path.suffix:
        case ".json":
            return json.loads(file)
        case ".yml" | ".yaml":
            return yaml.load(file, Loader=yaml.SafeLoader)
        case _:
            raise UnsupportedFileFormat(file_path.suffix)
