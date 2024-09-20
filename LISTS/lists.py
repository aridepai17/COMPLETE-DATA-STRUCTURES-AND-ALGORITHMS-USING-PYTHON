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

#Slicing/Deletion of items in the list
yourlist = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
print(yourlist)

print(yourlist[0:2]) #prints [1, 2] from index 0 to 1
print(yourlist[2:5]) #prints [3, 4, 5] from index 2 to 4
print(yourlist[1:])
print(yourlist[:5]) #prints [1, 2, 3, 4, 5] from index 0 to 4

yourlist.pop(1) #removes the item at index 1
print(yourlist)
#Time Complexity: O(n)

yourlist.remove(5) #removes the item 5
print(yourlist)
#Time Complexity: O(n)

del yourlist[0] #removes the item at index 0
#Time Complexity: O(n)-
del yourlist[2:4] #removes the items from index 2 to 3
print(yourlist)

#Searching for an item in the list
ourlist = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
#in operator
target = 5
if target in ourlist:
    print(f'{target} is present in ourlist')
else:
    print(f'{target} is not present in ourlist')
#Time Complexity: O(n)

#Linear Search
def linearsearchlist(plist, ptarget):
    for i, value in enumerate(plist):
        if value == ptarget:
            return i
    return -1

linearsearchlist(ourlist, target)
#Time Complexity: O(n)
#Space Complexity: O(1)





