'''
for i in range(10):
    for j in range(10):
        if  (j+i)%2 == 0:
            print(chr(65+(j+i)%10), end=' ')
        else:
            print(chr(97+(j+i)%10), end=' ')
    print(end='\n')
'''

'''
for i in range(10):
    for j in range(10):
        print(chr(65+(j+i)%10) if (j+i)%2 == 0 else chr(97+(j+i)%10), end=' ')
    print(end='\n')
'''


for i in range(10): print(''.join(chr(65 + (j + i) % 10) if (j + i) % 2 == 0 else chr(97 + (j + i) % 10) for j in range(10)))