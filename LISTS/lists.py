#Accessing/Traversing the List
shoppinglist = ['Milk', 'Bread', 'Butter']
print(shoppinglist[0]) #prints Milk
print(shoppinglist[1]) #prints Bread
print(shoppinglist[2]) #prints Butter
print('Milk' in shoppinglist) #prints True
print('Eggs' in shoppinglist) #prints False
print(shoppinglist[-1]) #prints Butter
print(shoppinglist[-2]) #prints Bread
print(shoppinglist[-3]) #prints Milk

for i in shoppinglist:
    print(i) #Prints all the items in the list


#Updating/Insertion of items in the list
mylist = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
print(mylist)
mylist[2] = 30 #Updating the value at index 2
print(mylist) 
#Time Complexity: O(1)

minelist = ['abc', 'def', 'ghi']
print(minelist)
minelist.insert(2, 'xyz') #Inserting 'xyz' at index 2
#Time Complexity: O(n)
print(minelist)
minelist.append('pqr') #Inserting 'pqr' at the end of the list
print(minelist)
#Time Complexity: O(1)
newlist = [1, 2, 3, 4, 5]
minelist.extend(newlist) #Inserting the elements of newlist at the end of minelist
print(minelist)
#Time Complexity: O(n)