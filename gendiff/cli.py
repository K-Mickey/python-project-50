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

    path1, path2, fmt = args.first_file, args.second_file, args.format
    path1 = path1.resolve()
    path2 = path2.resolve()

    return path1, path2, fmt