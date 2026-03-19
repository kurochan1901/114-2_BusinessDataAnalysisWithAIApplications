from math import trunc, log  #  truncation function: find the integer part of float numbers
from decimal import *

getcontext().prec = 11   #  設定最大的精度範圍至小數點後第 10 位
n = 5                   #  問題的精度範圍 至小數點後第 5 位

def squareRoot(a):
    if a < 0:
        raise ValueError(' ****  a = ', a, ' :  < or = 0: ERROR !! ')

    ## Binary-Search Algorithm - SquareRoot
    lower, upper = 0, a
    if a < 1: upper = 1
    
    while round(Decimal(str(upper)),n) != round(Decimal(str(lower)),n):
        avg = Decimal(str(upper)) + Decimal(str(lower))
        avg = avg / Decimal(str(2.0))    
        if avg**2 >= a:
            upper = avg
        else:
            lower = avg
            
    sol = Decimal(str(trunc(upper * 10**n))) / Decimal(str(10**n))
    print(' squareRoot(', a, ') = ', sol)
    return [a, 2, sol]

squareRoot(100)
## squareRoot(1000000000)      #超出精度範圍
squareRoot(0.0001)
squareRoot(81)
## squareRoot(-9)                 #底數a需>=0
squareRoot(0)