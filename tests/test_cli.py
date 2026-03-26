from pathlib import Path
from unittest.mock import patch

from gendiff.cli import main


def test_main():
    with patch("sys.argv", ["gendiff", "file1.json", "file2.json"]):
        file1, file2, format_name = main()

    assert isinstance(file1, Path)
    assert isinstance(file2, Path)
    assert isinstance(format_name, str)
