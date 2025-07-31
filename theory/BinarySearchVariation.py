def binary_search_exact(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

def binary_search_leftmost(arr, target):
    l = 0
    r = len(arr) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            l = m + 1
        elif arr[m] < target:
            r = m - 1
        else:
            i = m
            r = m - 1
            
    return i

def binary_search_rightmost(arr, target):
    l = 0
    r = len(arr) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            l = m + 1
        elif arr[m] < target:
            r = m - 1
        else:
            i = m
            l = m + 1
            
    return i


