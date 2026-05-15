#----------------------------------------------------
# [ Module ]: TWSE_Crawler.py
# < TWSE 個股資料下載模組 >：
#----------------------------------------------------

def twse_crawler(year=2019, mm=5, dd=22, stockNo=2330):
    ''' 例如： year=2019 mm=05 dd=02 stockNo=2330 '''
    import bs4 as bs  #  beautifulsoup 4
    import urllib
    import urllib.request

    #----------------------------------------------------
    # 1. 連線至台灣證交所 (TWSE)，擷取 個股資料
    #----------------------------------------------------
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='
    url_history = url_twse + str(year) + str(mm).zfill(2) + str(dd).zfill(2) + '&stockNo=' + str(stockNo)
    print(url_history)
    webpage_history = urllib.request.urlopen(url_history)
    web_html = bs.BeautifulSoup(webpage_history, 'html.parser')
    print(web_html)

    import json
    stock = json.loads(web_html.text)  #  讀取 JSON 資料
    stock

    #----------------------------------------------------
    # 2. 轉換 個股資料成 data frame 資料格式
    #----------------------------------------------------
    stock_info = list(stock.values())  #  轉換成 list 格式
    stock_info
    # stock_info[2]
    # stock_info[3]

    import pandas as pd
    import numpy as np

    stock_price = pd.DataFrame(stock_info[4])
    stock_price

    ##  將 data frame 資料加上 column name
    stock_price.columns = stock_info[3]
    stock_price

    ## 將第一個 column name “日期” 改成 個股 title 
    stock_info[3][0] = stock_info[2]
    stock_price.columns = stock_info[3]
    stock_price

    ## 將 index 欄位 改成 個股 title 
    df_price = stock_price.set_index(stock_price.columns[0])
    df_price

    #----------------------------------------------------
    # < 輸出個股資料至 csv 檔案 >
    #----------------------------------------------------
    import os.path
    mydir ='./'      #  檔案路徑
    #  建立檔案路徑 + 檔案名稱 stock.csv
    csv_file = os.path.join(mydir, "stock" + str(stockNo) + '_' + str(year) + str(mm).zfill(2) + ".csv")
    df_price.to_csv(csv_file, encoding='utf_8_sig')   #  輸出 csv 檔案 
    print(' 輸出 csv 檔案 : ', csv_file)
    return df_price  #   回傳 個股 data frame 資料
    
'''
twse_crawler()
'''
