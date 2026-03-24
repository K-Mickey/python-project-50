from gendiff import cli, generate_diff


def main():
    file_path1, file_path2, format_ = cli.main()
    result = generate_diff(file_path1, file_path2)
    print(result)


if __name__ == '__main__':
    main()