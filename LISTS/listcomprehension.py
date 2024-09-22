prevlist = [1, 2, 3]
newlist = [i * 2 for i in prevlist]
print(prevlist) # prints [1, 2, 3]
print(newlist) # prints [2, 4, 6]

language = 'Python'
newlanguage = [letter for letter in language]
print(newlanguage) # prints ['P', 'y', 't', 'h', 'o', 'n']

#Conditional List Comprehension
previouslist = [-1, 10, -20, 2, -90, 60, 45, 20]
latestlist = [no for no in previouslist if no > 0]
anotherlist = [no * no for no in previouslist if no < 0]
print(latestlist) #prints [10, 2, 60, 45, 20]
print(anotherlist) #prints [1, 400, 8100] 