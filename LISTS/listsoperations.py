#Concatenation using + operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

#* operator
list4 = list1 * 3
print(list4)

#len() operator: returns count of elements in the list
list5 = [1, 2, 3, 4, 5]
print(len(list5))

#max() operator: returns maximum value in the list
list6 = [1, 2, 3, 4, 5]
print(max(list6))

#min() operator: returns minimum value in the list
list7 = [1, 2, 3, 4, 5]
print(min(list7))

#sum() operator: returns sum of all the elements in the list
list8 = [1, 2, 3, 4, 5]
print(sum(list8))

#Average of numbers program using list()
mylist = list()
while(True):
    inputnumber = int(input('Enter a number: '))
    if inputnumber == 'done':
        break
    value = float(inputnumber)
    mylist.append(value)
    
average = sum(mylist) / len(mylist)
print('Average:', average)