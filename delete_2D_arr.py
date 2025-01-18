# Deletion in 2D array

from array import *
array2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
del array2[1]
for x in array2:
    for y in x:
        print(y, end=' ')
    print()