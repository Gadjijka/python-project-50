from gendiff.cli import arg_parser
from gendiff.base_logic import make_a_difference
from gendiff.formats.format import choice_format


def main():
    args = arg_parser()
    print choice_format(make_a_difference(args.first_file, args.second_file), args.format)


if __name__ = "__main__":
    main()
