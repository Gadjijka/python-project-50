import argparse


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and show a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format output',
        default='stylish',
        type=str
    )
    return parser.parse_args()
