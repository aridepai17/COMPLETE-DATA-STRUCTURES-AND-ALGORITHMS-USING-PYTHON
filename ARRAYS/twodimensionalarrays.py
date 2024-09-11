import numpy as np

#Creation of two dimensional array
twodarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twodarray)

#Inserting column in two dimensional array
newtwodarray = np.insert(twodarray, 1, [[1, 2, 3, 4]], axis=1)
print(newtwodarray)

newtwodarray = np.append(twodarray, [[1, 2, 3, 4]], axis=0)
print(newtwodarray)
