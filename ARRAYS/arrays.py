# Inserting an element in an Array
import array

myarray1 = array.array('i', [1, 2, 3, 4, 5])
print(myarray1)
myarray1.insert(5, 6)
print(myarray1)  
# Time Complexity: O(n)
# Space Complexity: O(1)

# Traversal Operation in Arrays
from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [2.5, 3.2, 3.3])

arr1.insert(2, 9)
print(arr1)

def traversalarray(array):
    for i in array: # O(n)
        print(i)    # O(1)
        
traversalarray(arr1)
# Time Complexity: O(n)
# Space Complexity: O(1)

# Access Array Element 
def accesselement(array, index):
    if index > len(array): # O(1)
        print("There is not any element in this index") # O(1)
    else:
        print(array[index]) # O(1)
        
accesselement(arr1, 2)
# Time Complexity: O(1)
# Space Complexity: O(1)
