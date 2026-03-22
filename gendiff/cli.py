import argparse
from pathlib import Path


class FileNotFoundError(Exception):
    def __init__(self, file):
        message = f'File {file} does not exist'
        super().__init__(message)


def main() -> tuple[Path, Path, str]:
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
    )

    parser.add_argument('first_file', type=Path)
    parser.add_argument('second_file', type=Path)
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='default',
    )

    args = parser.parse_args()

    file1, file2, format_ = args.first_file, args.second_file, args.format
    file1 = file1.resolve()
    file2 = file2.resolve()

    for file in (file1, file2):
        if not file.exists():
            raise FileNotFoundError(file)

    return file1, file2, format_