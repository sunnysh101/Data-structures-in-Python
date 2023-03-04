# How to create an array in Python

import array as arr

# Using the list
arr1 = [11, 52, 43, 34, 25]

# Using the array module
arr_int = arr.array('i', [1,2,3,4,5])
arr_float = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
arr_str = arr.array('u', ['a', 'b', 'c', 'd', 'e'])

# The reason why list is used to create an array is that it is more flexible and can be used to create an array of any data type.
# However, the array module is more efficient and is used to create an array of a single data type.

# To access the elements of an array, we can use the index operator [].
print(arr1[1])


# To add an element to an array, we can use the append() method.
arr1.append(6)
print(arr1)

# To insert an element at a specific position, we can use the insert() method.
arr1.insert(2, 56)
print(arr1)

# To remove an element from an array, we can use the remove() method.
arr1.remove(56)
print(arr1)

# To remove the last element of an array, we can use the pop() method.
arr1.pop()
print(arr1)

# To find the length of an array, we can use the len() method.
print(len(arr1))

# To sort the array, we can use the sort() method.
arr1.sort()
print(arr1)

# To sort an array using loops
# This is a bubble sort algorithm and it's complexity is O(n^2),  bad for large arrays.
for i in range(len(arr1)):
    for j in range(i+1, len(arr1)):
        if arr1[i] > arr1[j]:
            arr1[i], arr1[j] = arr1[j], arr1[i]

print(arr1)

# To reverse the array, we can use the reverse() method.
arr1.reverse()
print(arr1)

# To check if an element exists in an array, we can use the in operator.
print("11 in array?", 11 in arr1)
print("10 in array?", 10 in arr1)

# TO count the number of occurrences of an element in an array, we can use the count() method.
arr1.append(11)
print("11 occurs", arr1.count(11), "times")

# To copy an array, we can use the copy() method.
arr2 = arr1.copy()
print(arr2)

# Extend is used to add multiple elements to an array.
# To extend an array, we can use the extend() method.
arr1.extend([7,8,9])
print(arr1)