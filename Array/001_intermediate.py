# This is an intermediate level of python array.

# To create a 2D array, we can use the following approach.
arr2D = [[1,2,3], [4,5,6], [7,8,9]]

# To flatten a 2d array, we can use the following approach.
arr1D = [x for row in arr2D for x in row]
print(arr1D)

# To marge two arrays in a single array
arr1 = [1,2,3]
arr2 = [4,5,6]
arr3 = arr1 + arr2

print(arr3)

# To find the largest and smallest element in an array, we can use the following approach.
arr = [1,2,3,4,5,6,7,8,9,10]
print("Largest element in array:", max(arr))
print("Smallest element in array:", min(arr))


# TO find the sum of all elements in an array, we can use the following approach.
print("Sum of all elements in array:", sum(arr))

# To check if two arrays are equal, we can use the following approach.
arr1 = [1,2,3]
arr2 = [1,2,3]
print("Are arrays equal?", arr1 == arr2)


# To remove duplicate elements from an array, we can use the following approach.
arr = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
arr = list(set(arr))
print(arr)

# TO find the median of an array
arr = [1,2,3,4,5,6,7,8,9,10]
arr.sort()
print("Median of array:", arr[len(arr)//2])
