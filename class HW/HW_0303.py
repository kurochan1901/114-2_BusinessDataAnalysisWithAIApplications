from decimal import Decimal, getcontext
from math import sqrt

n = 30
m = 30
getcontext().prec = 60

a,b,c,d,count = 1,1,1,1,0

# <Method 1>
while round(Decimal(str(1+a/b)), n) - round(Decimal(str(b/a)), n) != 0:
    a, b, count = Decimal(b), Decimal(a+b), count+1
    
print('n =', n, 'count =', count, ': \t a =', a, '\t b =', b)
print('\t\t\t\t\t 123456789_123456789_123456789_123456789',
      '\n精確至第', n, '位數 :\t  b/a = \t', (Decimal(b/a)),
      '\n精確至第', n, '位數 :\t (a+b/b)) = \t', (Decimal(1+a/b)))

# <Method 2>
count = 0
while abs((Decimal(str(1+c/d)) / Decimal(str(d/c))) - Decimal(str(1.0))) > 10**(-(n+1)):
    c, d, count = Decimal(d), Decimal(c+d), count+1

print('m =',m, 'count =', count, ': \t c =', c, '\t d =', d)
print('\t\t\t\t\t 123456789_123456789_123456789_123456789',
      '\n精確至第', m, '位數 :\t  d/c = \t', (Decimal(d/c)),
      '\n精確至第', m, '位數 :\t (c+d/d)) = \t', (Decimal(1+c/d)))

print('\n精確⾄第 50 位數 :   Correct Answer = \t', 
        Decimal('1.61803398874989484820458683436563811772030917980576'))