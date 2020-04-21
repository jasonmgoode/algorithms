"""Binary Search"""

def recursive_binary_search(arr, target, start, end):
    """Recursively reduce the size of array.

    :params
        arr: a sorted array of unique ints
        target: target number to locate in the array
        start: start index of arr
        end: end index of arr

    :returns
        the index of array element matching the target, 
        or False if it does not exist

    """

    # bottom out if the full array has been searched
    # but no match was found
    if end < 0 or start > end:
        return False
    
    # choose a pivot element at the midpoint of the array
    pivot = (start + end) // 2

    # if the pivot matches the target, return the index
    if target == arr[pivot]:
        return pivot

    elif target < arr[pivot]:
        # search to the left of the pivot 
        return recursive_binary_search(arr, target, start, pivot-1)
    else:
        # search to the right of the pivot
        return recursive_binary_search(arr, target, pivot + 1, end)

def iterative_binary_search(arr, target):
    """Iterate array, removing as you go.
    
    Params:
        arr: a sorted array of unique ints
        target: target number to locate in the array

    Returns:
        the index of array element matching the target, 
        or False if it does not exist

    """

    start = 0
    end = len(arr) - 1

    while start <= end:
        # set pivot as midpoint of a sorted array
        pivot = (start + end) // 2
        
        # if pivot == target, return index of pivot
        if target == arr[pivot]:
            return pivot
        
        # if target < pivot, look at left side only
        elif target < arr[pivot]:
            end = pivot - 1
        
        # if target > pivot, look at right side only
        else:
            start = pivot + 1

    return False
