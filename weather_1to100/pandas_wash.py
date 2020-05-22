# 讀取 CSV File
import pandas as pd # 引用套件並縮寫為 pd
import time
df = pd.read_csv('ALL_MLB_Weather.csv',encoding='utf-8')

print(df)
df= df.dropna()
print(df)
df = df.drop(columns=['Unnamed: 0'])
print(df)

df.index = range(len(df))
df=df.reset_index()
df=df.drop(['index'],axis=1)
print(df)

def column_filter(s):
    return s.split('°')[0].strip()

df['feel1'] = df['feel1'].apply(column_filter)
df['feel2'] = df['feel2'].apply(column_filter)
df['feel3'] = df['feel3'].apply(column_filter)
df['temp1'] = df['temp1'].apply(column_filter)
df['temp2'] = df['temp2'].apply(column_filter)
df['temp3'] = df['temp3'].apply(column_filter)

def column_filter2(s):
    return s.split('%')[0].strip()
df['precip1'] = df['precip1'].apply(column_filter2)
df['precip2'] = df['precip2'].apply(column_filter2)
df['precip3'] = df['precip3'].apply(column_filter2)

def column_filter3(s):
    return s[:4].strip()
print(df['speed1'].apply(column_filter3))

df['speed1'] = df['speed1'].apply(column_filter3)
df['speed2'] = df['speed2'].apply(column_filter3)
df['speed3'] = df['speed3'].apply(column_filter3)

def  convert_to_24(time):
    if time[-3:-1] == "AM":
        return time[:-3] + ':00'
    elif int(str(int(time.split(':')[0]) + 12)) >= 24:
        return time[:-3] + ':00'
    else:
        return str(int(time.split(':')[0]) + 12)+':' + time.split(':')[1][:-3] + ':00'


print(df['time'].apply(convert_to_24))

df['time'] = df['time'].apply(convert_to_24)


def column_filter4(s):
    return s.strip()


df['park'] = df['park'].apply(column_filter4)
df['fightteam1'] = df['fightteam1'].apply(column_filter4)
df['fightteam2'] = df['fightteam2'].apply(column_filter4)
df['weather1'] = df['weather1'].apply(column_filter4)
df['weather2'] = df['weather2'].apply(column_filter4)
df['weather3'] = df['weather3'].apply(column_filter4)





df = df[(~df['weather1'].isin(['N/A']))&(~df['weather1'].isin(['N/A']))&(~df['weather3'].isin(['N/A']))]


df.to_csv(r'887788.csv',index=0, encoding='utf-8')





#df.to_csv(r'clean_mlb_weather.csv', encoding='utf-8')