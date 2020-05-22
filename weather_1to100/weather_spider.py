import requests
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse


headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# 爬取0-I個表格 後面加引數時檔案會以bs4匯出 即可進行第二次SELECT
column_list = ['date','time','park','fightteam1','fightteam2','weather1','weather2','weather3','temp1','temp2','temp3'\
,'feel1','feel2','feel3','precip1','precip2','precip3','speed1','speed2','speed3'\
,'dir1','dir2','dir3','PA', 'wOBA', 'BA', 'OBP', 'SLG', 'H', '1B', '2B', '3B', 'HR', 'RBI', 'BB', 'IBB', 'HBP',\
'SO', 'SAC', 'SF', 'GIDP', 'GROUND', 'LINE', 'POP', 'FLY',]

url = 'https://swishanalytics.com/mlb/weather?date=2014-08-30'
for aa in range (0, 1):

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')




    games_in_a_day = []
    for i in range(0,50):
        try:
            games_in_one_row=[]
            title = soup.select('div[class="row overall-account-margin"]')[i]
            fight_date = soup.select('small[class="lato mar-0 text-muted"]')[0]
            fight_dateee = fight_date.text
            fight_datee = fight_dateee.replace('GO TO TODAY', '')
            print(fight_datee)
            pa = parse(fight_datee)
            Fight_Date = pa.strftime('%Y-%m-%d')
            print(Fight_Date)
            games_in_one_row.append(Fight_Date)
            # print(games_in_one_row)


            # print(title) 表格之標籤
            fight_park = title.select('small[class="text-muted text-center desktop-hide"]')
            for p in fight_park:
                fight_park_text = p.text
                fight_time = fight_park_text.split('|', )[0]
                fight_parkx = fight_park_text.split('|' ,)[1]
                # print(fight_time)
                # print(fight_parkx)
            games_in_one_row.append(fight_time)
            games_in_one_row.append(fight_parkx)
            # print(games_in_one_row)
            #對戰場地以及開戰時間

            fight_team = title.select('h4[class="lato inline vert-mid bold"]')
            for t in fight_team:
                fight_team_text = t.text
                # print(fight_team_text)

                fit = fight_team_text.split('\xa0\xa0@\xa0\xa0')
            games_in_one_row.append(fit[0])
            games_in_one_row.append(fit[1])
            # print(games_in_one_row)
            # 對決隊伍名稱爬取
            fight_weather = title.select('td[class="text-center hour-width gametime-hour"]')


            for w in fight_weather:
                fight_weather_text = w.text
                # print(fight_weather_text)
                games_in_one_row.append(fight_weather_text)
            # print(games_in_one_row)
            # 天氣


            fight_temp = title.select('td[class="text-center gametime-hour"]')
            for a in fight_temp:
                fight_temp_text = a.text
                # print(fight_temp_text)
                games_in_one_row.append(fight_temp_text)
            # print(games_in_one_row)
            #對戰時其餘數據
            fight_forecast_data = title.select('table[class="table table-bordered mar-bottom-5"]')[0]
            fight_forecast_data_x = fight_forecast_data.select('td')
            for d in fight_forecast_data_x:
                fight_forecast_data_x.text = d.text
                # print(fight_forecast_data_x.text)
                games_in_one_row.append(fight_forecast_data_x.text)
            games_in_a_day.append(games_in_one_row)
            for i in games_in_a_day:
                if len(games_in_a_day) > 20:
                    games_in_a_day.append(games_in_one_row)

                else:
                    break
        except:
            break


    last_page_url = soup.select('a[class="text-muted"]')[2]['href']
    last_page_url = 'https://swishanalytics.com/'+last_page_url

    url = last_page_url

    print(url)

    data = pd.DataFrame(games_in_a_day,columns=column_list)
    data.to_csv(f'{Fight_Date}.csv',encoding='utf-8')
