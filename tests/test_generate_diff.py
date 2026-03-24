from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA_PATH = Path('tests/test_data/generate_diff')


@pytest.fixture
def file_path1():
    return TEST_DATA_PATH / 'file1.json'


@pytest.fixture
def file_path2():
    return TEST_DATA_PATH / 'file2.json'


@pytest.fixture
def empty_file_path():
    return TEST_DATA_PATH / 'empty_file.json'


def test_main_scenario(file_path1, file_path2):
    diff = generate_diff(file_path1, file_path2)

    result_path = TEST_DATA_PATH / 'result_main_scenario.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_identical_files(file_path1):
    diff = generate_diff(file_path1, file_path1)

    result_path = TEST_DATA_PATH / 'result_identical_files.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_empty_first_file(empty_file_path, file_path2):
    diff = generate_diff(empty_file_path, file_path2)

    result_path = TEST_DATA_PATH / 'result_empty_first_file.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_empty_second_file(file_path1, empty_file_path):
    diff = generate_diff(file_path1, empty_file_path)

    result_path = TEST_DATA_PATH / 'result_empty_second_file.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff
