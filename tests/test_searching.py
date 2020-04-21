import pytest

from searching.binary_search import (
    iterative_binary_search,
    recursive_binary_search,
)

@pytest.fixture
def sorted_arr():
    return [0, 1, 5, 6, 14, 22, 33, 68, 72]


def test_binary_search_iterative(sorted_arr):
    """Test iterative & recursive binary search"""
    # target in array
    target = 14
    assert iterative_binary_search(sorted_arr, target) == 4
    assert recursive_binary_search(sorted_arr, target, 0, len(sorted_arr)-1) == 4

    # target not in array
    target = 7
    assert iterative_binary_search(sorted_arr, target) is False
    assert recursive_binary_search(sorted_arr, target, 0, len(sorted_arr)-1) is False
