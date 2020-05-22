import pandas as pd
import  pymysql
import pandas
import csv


mydb = pymysql.connect(host='1.tcp.jp.ngrok.io',port=23879 , user="arthur", passwd="clubgogo", db="MoneyBallDatabase")
cursor = mydb.cursor()

with open('887788.csv', mode='r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    headers = next(rows)
    times = 1
    for row in rows:
        try:
            cursor.execute('INSERT INTO mlb_weather(Fight_date, Fight_time,\
             Fight_park, Fight_team1, Fight_team2, Fight_weather1, \
             Fight_weather2, Fight_weather3, Fight_temp1, Fight_temp2,\
              Fight_temp3, Fight_feel1, Fight_feel2, Fight_feel3,\
               Fight_precip1, Fight_precip2, Fight_precip3,\
                Speed1, Speed2, Speed3, Dir1, Dir2, Dir3, PA,\
                 wOBA, BA, OBP, SLG, H, B1B, B2B, B3B, HR, RBI, BB, IBB,\
                  HBP, SO, SAC, SF, GIDP, GROUND, LINE, POP, FLY)'\
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\
                , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\
                , %s, %s, %s\
                , %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
        except pymysql.err.ProgrammingError as e:
            print(e.args)
            times += 1
            continue
        print('Now is done {}'.format(times))
mydb.commit()
#close the connection to the database.
cursor.close()
print("Done")