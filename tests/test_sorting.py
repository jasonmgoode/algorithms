import pytest

from sorting.sorting import (
    insertion_sort, 
    merge_sort,
    quick_sort,
)

@pytest.fixture
def mock_arr():
    return [5, 0, 88, 2.2, -4, 7, 1, 8, 22, 8]

def test_insertion_sort(mock_arr):

    sorted_arr = insertion_sort(mock_arr)
    assert sorted_arr == [-4, 0, 1, 2.2, 5, 7, 8, 8, 22, 88]


def test_merge_sort(mock_arr):
    
    sorted_arr = merge_sort(mock_arr)
    assert sorted_arr == [-4, 0, 1, 2.2, 5, 7, 8, 8, 22, 88]

def test_quick_sort(mock_arr):
    sorted_arr = quick_sort(mock_arr)
    assert sorted_arr == [-4, 0, 1, 2.2, 5, 7, 8, 8, 22, 88]
