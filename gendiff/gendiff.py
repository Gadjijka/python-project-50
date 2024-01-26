import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', dest="FORMAT", help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def generate_diff(file_path1, file_path2):
    base1 = json.load(open(file_path1))
    base2 = json.load(open(file_path2))
    base_result_to_str = '{'
    for k, v in base1.items():
        if base2.get(k, None) != None:
            if v == base2[k]:
                base_result_to_str += f'\n {k}: {v}'
            else:
                base_result_to_str += f'\n - {k}: {v}'
                base_result_to_str += f'\n + {k}: {base2[k]}'
        else:
            base_result_to_str += f'\n - {k}: {v}'
    for k, v in base2.items():
        if base1.get(k, None) == None:
            base_result_to_str += f'\n + {k}: {v}'
    base_result_to_str += '\n }'
    print(base_result_to_str)


if __name__ == "__main__":
    main()
