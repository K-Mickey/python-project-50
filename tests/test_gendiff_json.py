from pathlib import Path

import pytest

from gendiff import generate_diff
from gendiff.gendiff import FormatName

TEST_DATA_PATH = Path("tests/test_data")


@pytest.fixture
def simple_file_path1():
    return TEST_DATA_PATH / "simple_tree1.json"


@pytest.fixture
def simple_file_path2():
    return TEST_DATA_PATH / "simple_tree2.json"


@pytest.fixture
def deep_file_path1():
    return TEST_DATA_PATH / "deep_tree1.json"


@pytest.fixture
def deep_file_path2():
    return TEST_DATA_PATH / "deep_tree2.json"


def test_main_case(simple_file_path1, simple_file_path2):
    diff = generate_diff(simple_file_path1, simple_file_path2)

    result_path = TEST_DATA_PATH / "result_simple_tree.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_identical_files(simple_file_path1):
    diff = generate_diff(simple_file_path1, simple_file_path1)

    result_path = TEST_DATA_PATH / "result_identical_files.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_deep_tree(deep_file_path1, deep_file_path2):
    diff = generate_diff(deep_file_path1, deep_file_path2)

    result_path = TEST_DATA_PATH / "result_deep_tree_stylish.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_plain_format(deep_file_path1, deep_file_path2):
    diff = generate_diff(
        file_path1=deep_file_path1,
        file_path2=deep_file_path2,
        format_name=FormatName.PLAIN,
    )

    result_path = TEST_DATA_PATH / "result_deep_tree_plain.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_json_format(deep_file_path1, deep_file_path2):
    diff = generate_diff(
        file_path1=deep_file_path1,
        file_path2=deep_file_path2,
        format_name=FormatName.JSON,
    )

    result_path = TEST_DATA_PATH / "result_deep_tree_json.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff
