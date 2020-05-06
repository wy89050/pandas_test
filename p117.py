# Pandas DataFrame JSON資料
# 環保署 紫外線資料來源:  https://opendata.epa.gov.tw/Data/Contents/UV/

import pandas as pd

pd.set_option('display.unicode.east_asian_width', True) #調整顯示文字寬度

df = pd.read_json('https://bit.ly/2Qfzovb')  #是json格式的網址

df['UVI'] = pd.to_numeric(df['UVI']) #文字轉換成數字

df = df.sort_values(by='UVI', ascending=False) #排序資料

df = df.drop(columns=['SiteName']) #移除不要的欄

df = df.rename(columns={'County': '城市', #重設欄位名稱
'PublishTime':'發布時間' ,'UVI':'紫外線指數'})

df = df.reset_index(drop=True) #重設索引

print(df.head(5)) #取出前五名