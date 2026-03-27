from pathlib import Path
from unittest.mock import patch

import pytest

from gendiff.cli import main
from gendiff.gendiff import FormatName


def test_main():
    with patch("sys.argv", ["gendiff", "file1.json", "file2.json"]):
        file1, file2, format_name = main()

    assert isinstance(file1, Path)
    assert isinstance(file2, Path)
    assert isinstance(format_name, FormatName)


def test_format_name_default():
    with patch("sys.argv", ["gendiff", "file1.json", "file2.json"]):
        _, _, format_name = main()

    assert format_name == FormatName.STYLISH


def test_format_name_error():
    with pytest.raises(SystemExit):
        with patch(
            "sys.argv", ["gendiff", "file1.json", "file2.json", "-f", "fake"]
        ):
            _, _, format_name = main()
