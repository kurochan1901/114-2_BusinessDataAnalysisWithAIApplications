# -*- coding: utf-8 -*-

for i in range(10):
    for j in range(10):
        if (j + i) % 2 == 0:
            print(chr(65 + (j + i) % 10), end='')
        else:
            print(chr(97 + (j + i) % 10), end='')
    print(end='\n')
    
for i in range(10): print(''.join(chr(65+(j+i)%10) if (j+i)%2 == 0 else chr(97+(j+i)%10) for j in range(10)))

print(''.join(chr(65 + (j + i) % 10) if (j + i) % 2 == 0 else chr(97 + (j + i) % 10) for j in range(10)) for i in range(10))
#why?

a = [''.join(chr(65 + (j + i) % 10) if (j + i) % 2 == 0 else chr(97 + (j + i) % 10) for j in range(10)) for i in range(10)]
#join: 串接字串(比較方便)   
#chr(65 + (j + i) % 10) if (j + i) % 2 == 0 else chr(97 + (j + i) % 10) for j in range(10)) => 這裡是個 generator expression，會產生一個 generator 物件
#所以不能直接使用 join 來串接。需要先將 generator 物件轉換成 list 或 tuple 才能使用 join。
