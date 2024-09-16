import numpy as np

#Creation of two dimensional array
twodarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twodarray)

#Inserting column in two dimensional array
newtwodarray = np.insert(twodarray, 1, [[1, 2, 3, 4]], axis=1)
print(newtwodarray)

newtwodarray = np.append(twodarray, [[1, 2, 3, 4]], axis=0)
print(newtwodarray)

#Accessing elements of two dimensional array
twodarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twodarray)

def accesselements(array, rowindex, columnindex):
    if rowindex >= len(array) and columnindex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowindex][columnindex])
        
accesselements(twodarray, 1, 2)
#Time Complexity: O(1)
#Space Complexity: O(1)

#Traversing a two dimensional array
twodarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twodarray)

def traversetwodarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
traversetwodarray(twodarray)
#Time Complexity: O(n*m)
#Space Complexity: O(1)

#Searching for element in two dimensional array
twodarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twodarray)

def searchtwodarray(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return 'Element found at index: '+str(i)+', '+str(j)
    return 'Element not found'

print(searchtwodarray(twodarray, 17))
#Time Complexity: O(n*m)
#Space Complexity: O(1)

#Deletion of element in two dimensional array
twodarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twodarray)

newtwodarray = np.delete(twodarray, 1, axis=0)
print(newtwodarray)
#Time Complexity: O(n*m)
#Space Complexity: O(1)
            
