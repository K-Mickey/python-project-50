import argparse
from pathlib import Path


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

    file_path1, file_path_2, format_ = args.first_file, args.second_file, args.format
    file_path1 = file_path1.resolve()
    file_path_2 = file_path_2.resolve()

    return file_path1, file_path_2, format_