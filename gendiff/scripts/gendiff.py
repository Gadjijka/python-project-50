from gendiff.cli import arg_parser
from gendiff.generate_diff import generate_diff


def main():
    args = arg_parser()
    print(generate_diff(args.first_file, args.second_file), args.format)


if __name__ == "__main__":
    main()
