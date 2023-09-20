'''
k = 1
s = 0
for i in range(1000000):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2
print(round(s,10))
'''

'''
from math import acos
def printValueOfPi():
    pi = round(2 * acos(0.0), 10)
    print(pi)
if __name__ == "__main__":
    printValueOfPi()
'''

import random
import statistics
def throwNeedles(numNeedles):
    incircle=0
    for Needles in range(1,numNeedles+1):
        x=random.random()
        y=random.random()
        if(x*x+y*y)<=1:
            incircle+=1
    return 4*(incircle/numNeedles)
print(throwNeedles(10000000000))    