from gendiff import cli, generate_diff


def main():
    path1, path2, format_name = cli.main()
    result = generate_diff(
        file_path1=path1,
        file_path2=path2,
        format_name=format_name,
    )
    print(result)


if __name__ == "__main__":
    main()
