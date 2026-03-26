from math import trunc, log  #  truncation function: find the integer part of float numbers
from decimal import *

getcontext().prec = 31   #  設定最大的精度範圍至小數點後第 10 位
n = 25                   #  問題的精度範圍 至小數點後第 5 位

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

def CubeRoot(a):
    if a >= 1: 
        lower, upper = 0, a
    else:
        lower, upper = a, 1

    while round(Decimal(str(upper)),n) != round(Decimal(str(lower)),n):
        avg = Decimal(str(upper)) + Decimal(str(lower))
        avg = avg / Decimal(str(2.0))
        if avg**3 >= a:
            upper = avg
        else:
            lower = avg

    sol = Decimal(str(trunc(upper * 10**n))) / Decimal(str(10**n))
    print(' CubeRoot(', a, ') = ', sol)
    return [a, 3, sol]

def NthRoot(a, m):
    if m < 0:
        raise ValueError(' ****  m = ', m, ' :  < 0: ERROR !! ')
    elif m % 2 == 0:
        if a < 0:
            raise ValueError(' ****  a = ', a, ' :  < 0: ERROR !! ')
        elif 0 < a < 1:
            lower, upper = a, 1
        else:
            lower, upper = 0, a
    else:
        if a < 0:
            lower, upper = a, 0
        elif 0 < a < 1:
            lower, upper = a, 1
        else:
            lower, upper = 0, a
    
    while round(Decimal(str(upper)),n) != round(Decimal(str(lower)),n):
        avg = Decimal(str(upper)) + Decimal(str(lower))
        avg = avg / Decimal(str(2.0))
        if avg**m >= a:
            upper = avg
        else:
            lower = avg

    sol = Decimal(str(trunc(upper * 10**m))) / Decimal(str(10**m))
    print(' NthRoot(', a, ', ', m, ') = ', sol)
    return [a, m, sol]

squareRoot(2)
squareRoot(0.25)

CubeRoot(3)
CubeRoot(0.027)
CubeRoot(0.125)

NthRoot(2, 5)
NthRoot(0.25, 5)
NthRoot(0.125, 5)