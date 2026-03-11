from math import trunc   #  truncation function: find the integer part of float numbers
from decimal import *

getcontext().prec = 31   #  設定最大的精度範圍至小數點後第 30 位
n = 25                   #  設定 問題的精度範圍 至小數點後第 25 位

a = float(input("Enter a positive number: "))

# if a < 0, then raise ValueError...
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
## -----------------------------------------------------------------    

print('\t\t\t  123456789_123456789_123456789_') 
print(' Upper of Square Root =', upper,' (', getcontext().prec-1,'位)')
print(' Lower of Square Root =', lower,' (', getcontext().prec-1,'位)')

print(20*'-' + '\n', a, '的平方根，精確至小數點後第 ', n,' 位 :')
print(' squareRoot(', a, ') =', sol)