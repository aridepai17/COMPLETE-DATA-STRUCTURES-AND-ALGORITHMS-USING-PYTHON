#list() function - converts string to list
a = 'spam'
b = list(a)
print(b) #prints ['s', 'p', 'a', 'm']

#split() function - converts string to list
a = 'spam spam spam'
b = a.split()
print(b) #prints ['spam', 'spam', 'spam']

a = 'spam1-spam2-spam3'
delimiter = '-'
b = a.split(delimiter)
print(b) #prints ['spam1', 'spam2', 'spam3']

#join() function - converts list to string
a = 'spam1-spam2-spam3'
delimiter = 'a'
b = a.split(delimiter)
print(b)
print(delimiter.join(b)) #prints 'spam1-spam2-spam3'