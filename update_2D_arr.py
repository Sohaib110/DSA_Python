# Update Operation on 2D Array

from array import *
array2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
array2[1] = [100, 200, 300]
for x in array2:
    for y in x:
        print(y, end=' ')
    print()