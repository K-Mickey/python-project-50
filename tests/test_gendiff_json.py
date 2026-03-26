from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA_PATH = Path("tests/test_data/gendiff_json")


@pytest.fixture
def simple_file_path1():
    return TEST_DATA_PATH / "simple_tree1.json"


@pytest.fixture
def simple_file_path2():
    return TEST_DATA_PATH / "simple_tree2.json"


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


def test_deep_tree():
    file_path1 = TEST_DATA_PATH / "deep_tree1.json"
    file_path2 = TEST_DATA_PATH / "deep_tree2.json"
    diff = generate_diff(file_path1, file_path2)

    result_path = TEST_DATA_PATH / "result_deep_tree.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff
