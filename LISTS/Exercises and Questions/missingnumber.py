"""
Write a function to find the missing number in a given integer 
array of 1 to 100. The function takes to parameter the 
array and the number of elements that needs to be in array.  
For example if we want to find missing number from 1 to 6 the 
second parameter will be 6. 
"""
def missingnumber(arr, n):
    total = (n * (n + 1)) // 2 #Calculate the sum of first n natural numbers
    sumarray = sum(arr) #Calculate the sum of the array
    missingnumber = total - sumarray
    return missingnumber

#Test the function
print(missingnumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    