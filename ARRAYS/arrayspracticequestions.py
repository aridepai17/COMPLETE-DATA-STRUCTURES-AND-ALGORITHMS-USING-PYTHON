from array import *

#1. Create an array and traverse
myarray = array('i', [1, 2, 3, 4, 5])

for i in myarray:
    print(i)
    
#2. Access individual elements through indexes
print("Accessing first element: ", myarray[0])
print("Accessing second element: ", myarray[1])
print("Accessing last element: ", myarray[-1])

#3. Append any value to the array using append method
myarray.append(6)
print("Array after appending: ", myarray)

#4. Insert value in an array using insert method
myarray.insert(2, 7)
print("Array after inserting: ", myarray)

#5. Extend python array using extend() method
myarray1 = array('i', [8, 9, 10])
myarray.extend(myarray1)
print("Array after extending: ", myarray)

#6. Add items from list into array using fromlist() method
templist = [11, 12, 13]
myarray.fromlist(templist)
print("Array after adding from list: ", myarray)

#7. Remove any array element using remove() method
myarray.remove(12)
print("Array after removing: ", myarray)

#8. Remove last array element using pop() method
myarray.pop()
print("Array after poping: ", myarray)

#9. Fetch any element through its index using index() method
print("Index of element 9: ", myarray.index(9))

#10. Reverse a python array using reverse() method
myarray.reverse()
print("Array after reversing: ", myarray)

#11. Get array buffer information through buffer_info() method
print("Array buffer information: ", myarray.buffer_info())

#12. Check for number of occurrences of an element using count() method
print("Number of occurrences of 9: ", myarray.count(9))

#13. Convert array to string using tostring() method
print("Array to string: ", myarray.tostring())

#14. Convert array to list using tolist() method
print("Array to list: ", myarray.tolist())

#15. Append a string to char array using fromstring() method
myarray.fromstring("14")
print("Array after adding string: ", myarray)

#16. Slice Elements from an array
print("Elements sliced: ", myarray[3:5])
