from gendiff import cli


def main():
    file1, file2, format_ = cli.main()

    for file in (file1, file2):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)


if __name__ == '__main__':
    main()