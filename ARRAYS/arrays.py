# Inserting an element in an Array
import array

myarray1 = array.array('i', [1, 2, 3, 4, 5])
print("Original array:", myarray1)
myarray1.insert(5, 6)  # Insert 6 at index 5
print("Array after insertion:", myarray1)
# Time Complexity: O(n)
# Space Complexity: O(1)

# Traversal Operation in Arrays
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])
arr2 = array.array('d', [2.5, 3.2, 3.3])

arr1.insert(2, 9)
print("Array after another insertion:", arr1)

def traversalarray(array):
    for i in array:  # O(n)
        print(i)      # O(1)

print("Traversing arr1:")
traversalarray(arr1)
# Time Complexity: O(n)
# Space Complexity: O(1)

# Access Array Element 
def accesselement(array, index):
    if index >= len(array):  # Fix: changed to >=
        print("There is not any element at this index")  # O(1)
    else:
        print("Element at index", index, "is:", array[index])  # O(1)

accesselement(arr1, 2)
# Time Complexity: O(1)
# Space Complexity: O(1)

# Linear Search
myarray2 = array.array('i', [1, 2, 3, 4, 5])

def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Linear search result:", linearsearch(myarray2, 5))
# Time Complexity: O(n)
# Space Complexity: O(1)

# Deleting an element
arr2 = array.array('i', [1, 2, 3, 4, 5])
arr2.remove(3)
print("Array after deletion:", arr2)
# Time Complexity: O(n)
# Space Complexity: O(1)
