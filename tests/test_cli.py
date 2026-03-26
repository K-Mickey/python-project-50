from pathlib import Path
from unittest.mock import patch

import pytest

from gendiff.cli import main


def test_main():
    with patch("sys.argv", ["gendiff", "file1.json", "file2.json"]):
        file1, file2, format_name = main()

    assert isinstance(file1, Path)
    assert isinstance(file2, Path)
    assert isinstance(format_name, str)


def test_format_name():
    with patch(
        "sys.argv", ["gendiff", "file1.json", "file2.json", "-f", "stylish"]
    ):
        _, _, format_name = main()

    assert format_name == "stylish"

    with pytest.raises(SystemExit):
        with patch(
            "sys.argv", ["gendiff", "file1.json", "file2.json", "-f", "fake"]
        ):
            _, _, format_name = main()
