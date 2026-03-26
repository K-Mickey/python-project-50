from pathlib import Path

from gendiff import generate_diff

TEST_DATA_PATH = Path("tests/test_data")


def test_main_case():
    file_path1 = TEST_DATA_PATH / "simple_tree1.yml"
    file_path2 = TEST_DATA_PATH / "simple_tree2.yml"
    diff = generate_diff(file_path1, file_path2)

    result_path = TEST_DATA_PATH / "result_simple_tree.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff


def test_deep_tree():
    file_path1 = TEST_DATA_PATH / "deep_tree1.yml"
    file_path2 = TEST_DATA_PATH / "deep_tree2.yml"
    diff = generate_diff(file_path1, file_path2)

    result_path = TEST_DATA_PATH / "result_deep_tree.txt"
    expected_diff = result_path.read_text()

    assert diff == expected_diff
