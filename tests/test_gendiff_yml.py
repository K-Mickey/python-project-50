from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA_PATH = Path('tests/test_data/gendiff_yml')


@pytest.fixture
def file_path1():
    return TEST_DATA_PATH / 'simple_case1.yml'


@pytest.fixture
def file_path2():
    return TEST_DATA_PATH / 'simple_case2.yml'


def test_main_case(file_path1, file_path2):
    diff = generate_diff(file_path1, file_path2)

    result_path = TEST_DATA_PATH / 'result_main_case.txt'
    expected_diff = result_path.read_text()

    assert diff == expected_diff
