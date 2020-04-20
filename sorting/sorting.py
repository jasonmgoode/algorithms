"""Sorting algorithms"""


def insertion_sort(arr):
    """Sort in place"""
    
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and key < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

    return arr

def merge_sort(arr):
    """"
    Sort recursively by breaking the array in half
    Then merge back together
    Complexity: O(n log n)
    """
    
    if len(arr) > 1:
        middle_idx = len(arr) // 2
        left_side = arr[:middle_idx]
        right_side = arr[middle_idx:]
        merge_sort(left_side)
        merge_sort(right_side)
        merge(left_side, right_side, arr)

    return arr

def merge(left_side, right_side, arr):
    """Recombine sorted subarrays"""
    # initialize indices
    # i = arr
    # j = left half
    # k = right half
    i = j = k = 0

    while j < len(left_side) and k < len(right_side):
        if left_side[j] < right_side[k]:
            arr[i] = left_side[j]
            j +=1
        else:
            arr[i] = right_side[k]
            k += 1
        i += 1

    while j < len(left_side):
        arr[i] = left_side[j]
        j+=1
        i+=1
    
    while k < len(right_side):
        arr[i] = right_side[k]
        k+=1
        i+=1

def quick_sort(arr):
    """Sort on a pivot element"""
    length = len(arr)

    if length <= 1:
        return arr
    
    else:
        # choose middle element in array as pivot 
        # & remove from array
        pivot = arr[length // 2]
        arr.pop(length//2)

    left_side = []
    right_side = []

    for element in arr:
        if element < pivot:
            left_side.append(element)
        else:
            right_side.append(element)
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)