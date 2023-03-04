# To implement binary search in an array, we can use the following approach.
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 5))

# To implement a binary search for unsorted array, we can use the following approach.
def binary_search_unsorted(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# TO implement a binary search for unsorted array using recursion, we can use the following approach.
def binary_search_unsorted_recursion(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_unsorted_recursion(arr, target, mid + 1, right)
    else:
        return binary_search_unsorted_recursion(arr, target, left, mid - 1)
    
