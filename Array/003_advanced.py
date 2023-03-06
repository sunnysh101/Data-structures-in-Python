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
# Binary search can be done on a sorted array only.
def binary_search_unsorted(arr, target):
    """This function will return the index of the target element in the array."""
    
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
    

arr = [21,32,31,42,5,26,73,82,191,10]
arr.sort()
print(binary_search_unsorted_recursion(arr , 26, 0, len(arr) - 1))
print(arr[3])

# to implement a selection sort, we can use the following approach.
# the complexity of selection sort is O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([21,32,31,42,5,26,73,82,191,10]))

print("Here is the implementation of merge sort")
# To implement a merge sort, we can use the following approach.
def merge_sort(arr):
    print(arr)
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive calls to sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted left and right halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Handle remaining elements in left or right half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        

arr = [4, 2, 8, 1, 3, 7, 5, 6,12]
merge_sort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# To implement a quick sort, we can use the following approach.
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([4, 2, 8, 1, 3, 7, 5, 6,12]))


# To implement radix sort, we can use the following approach.
def radix_sort(arr):
    max_num = max(arr)
    max_exponent = len(str(max_num))
    being_sorted = arr[:]
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position
        digits = [[] for i in range(10)]
        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
            except IndexError:
                digit = 0
            digit = int(digit)
            digits[digit].append(number)
        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)
    return being_sorted

print(radix_sort([4, 2, 8, 1, 3, 7, 51, 6,12]))

# To find the kth smallest element in an array, we can use the following approach.
def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]

print(kth_smallest([4, 2, 8, 1, 3, 7, 51, 6,12], 3))