# x can be any whole integer from 1-1000000
# y is going to be the x-val C(n)

import math
import matplotlib.pyplot as plt
import time
import numpy as np

starttime = time.time()

plt.xlabel('Log10(n)')
plt.ylabel('C(n)')

def collatz(x):
    count = 0
    while x != 1:   
        if x % 2 == 0:
            x=x/2
            count=count+1
        else:
            x=(x*3)+1
            count=count+1
    return count

x_coordinates = []
y_coordinates = []
for i in range(1, 1000001):
    x = math.log(i,10)
    x_coordinates.append(i) #append i or x???
    y = collatz(i)
    y_coordinates.append(y)

ymax=np.max(y_coordinates)#not sure if this is the way to go for finding maxy
xmax=collatz(ymax)

print('Max C(n) occurs at: x=',xmax,'and y=', ymax)

endtime = time.time() #don't want computation time to include plotting

total = endtime - starttime
print('Total time:', total,'secs')

plt.scatter(x_coordinates, y_coordinates)
plt.show()