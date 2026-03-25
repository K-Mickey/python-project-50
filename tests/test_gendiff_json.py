from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA_PATH = Path('tests/test_data/gendiff_json')


@pytest.fixture
def file_path1():
    return TEST_DATA_PATH / 'simple_case1.json'


@pytest.fixture
def file_path2():
    return TEST_DATA_PATH / 'simple_case2.json'


def test_main_case(file_path1, file_path2):
    diff = generate_diff(file_path1, file_path2)

    result_path = TEST_DATA_PATH / 'result_main_case.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_identical_files(file_path1):
    diff = generate_diff(file_path1, file_path1)

    result_path = TEST_DATA_PATH / 'result_identical_files.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff

