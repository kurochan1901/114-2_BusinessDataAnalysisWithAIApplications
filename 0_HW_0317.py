# HW2-Bubble_Sort_for_Lottery

from random import random
min_num = 1
max_num = 49
six_num = 6

yorn = 'y'
while yorn == 'y' or yorn == 'Y':
    max_dim = max_num - min_num + 1    # 初始設定號碼範圍：在1~49間
    
    lotto = []
    for i in range(max_dim):
        lotto.append(min_num + i);

    select = []
    for i in range(six_num):
        # 在1~49間：利用系統時間作為亂數種子，隨機選取號碼
        #           random() 回傳亂數值 介於 [0, 1)
        random_num = random() * 10000    
        lotto_num = int(random_num % max_dim)
        select.append(lotto[lotto_num])
        
        for j in range(lotto_num, max_dim-1):
            lotto[j] = lotto[j+1]        # 移除已經選中的號碼
        max_dim -= 1  # max_dim = max_dim - 1

    print("\n\n 本期樂透彩 電腦選號 如下：(1 ~ 49) \n\n")
    for i in range(six_num):
        print(select[i], end='\t')
    
    yorn = input("\n\n 是否繼續 電腦選號？(y/n)：")       