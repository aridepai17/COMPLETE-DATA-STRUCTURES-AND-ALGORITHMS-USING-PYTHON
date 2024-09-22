#Calculate Average Temperature

numdays = int(input("Enter number of days: "))
total = 0
temp = [ ]
for i in range(1, numdays + 1):
    nextday = input("Day " + str(i+1) + "'s high temperature: ")
    temp.append(nextday)
    total += temp[i]
    
average = round(total / numdays, 2)
print("Average temperature : " +str(average))

above = 0
for i in temp:
    if i > average:
        above += 1
print("Number of days above average : " + str(above))

