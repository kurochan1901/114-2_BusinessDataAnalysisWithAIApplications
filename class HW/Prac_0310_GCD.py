from math import trunc
from decimal import *

# GCD gratest common divisor 最大公因數
def gcd(a, b):
    if a < b:
        a, b = b, a         #確保 a 是較大的數
    while b != 0:
        a, b = b, a % b     #將 a 除以 b 的餘數賦值給 b，並將 b 的值賦值給 a
    return a                #當 b 為 0 時，a 就是最大公因數

#Fibonacci series: F(n+2) = F(n+1) + F(n)
# 列出a,b兩數之間的Fibonacci數列
def print_Fibonacci(a,b):
    lo, hi = (a, b) if a <= b else (b, a)

    x ,y = 0, 1
    while x < lo:
        x, y = y, x+y

    print(f"Fibonacci series in range {lo} to {hi}:",end=" ")
    found = False           #用來標記是否找到任何Fibonacci數字在範圍內
    while x <= hi:
        print(x, end=" ")
        found = True
        x, y = y, x+y

    if not found:
        print("No Fibonacci numbers in the specified range.")
    print()                 #換行  

#防呆
while True:                 #確保輸入有效的整數
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if a<=0 or b<=0:
            raise ValueError
            continue

        break               #兩者都合法，才跳出迴圈

    except ValueError:
        print("請輸入正整數，不能輸入小數或文字。再試一次。")

print("The GCD of", a, "and", b, "is", gcd(a, b))
print_Fibonacci(a, b)