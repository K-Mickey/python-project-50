import json
from pathlib import Path

FILE_ENCODING = 'utf-8'
INTEND_WIDTH = 2


def generate_diff(file_path1: Path, file_path2: Path) -> str:
    file1 = read_json_file(file_path1)
    file2 = read_json_file(file_path2)

    result = ['{']
    all_keys = sorted(file1.keys() | file2.keys())
    for key in all_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        is_key_removed = key not in file2
        is_key_added = key not in file1
        is_value_updated = value1 != value2

        if is_key_removed:
            result.append(format_line(key, value1, '-'))
        elif is_key_added:
            result.append(format_line(key, value2, '+'))
        elif is_value_updated:
            result.append(format_line(key, value1, '-'))
            result.append(format_line(key, value2, '+'))
        else:
            result.append(format_line(key, value1))

    result.append('}')
    return '\n'.join(result)


def read_json_file(file_path: Path) -> dict:
    with open(file_path, encoding=FILE_ENCODING) as file:
        return json.load(file)


def format_line(key: str, value: str, sign: str = ' ') -> str:
    return f'{INTEND_WIDTH * " "}{sign} {key}: {value}'