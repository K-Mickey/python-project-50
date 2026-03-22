import argparse


def main() -> tuple[str, str, str]:
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='default',
    )

    args = parser.parse_args()

    return args.first_file, args.second_file, args.format