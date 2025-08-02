import requests
import traceback
from time import sleep
import sqlite3
from datetime import datetime

# Подключение к базе данных
conn = sqlite3.connect('course_database.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    average_price TEXT NOT NULL,
    my_price TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()

headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU',
    'lang': 'ru-RU',
}

json_data = {
    'userId': 104098729,
    'tokenId': 'USDT',
    'currencyId': 'RUB',
    'payment': [
        '657',
    ],
    'side': '0',
    'size': '25',
    'page': '1',
    'amount': '2000',
    'vaMaker': False,
    'bulkMaker': False,
    'canTrade': True,
    'verificationFilter': 0,
    'sortType': 'OVERALL_RANKING',
    'paymentPeriod': [],
    'itemRegion': 1,
}

while True:
    
    try:
        response = requests.post('https://www.bybit.com/x-api/fiat/otc/item/online', headers=headers, json=json_data)

        if response.status_code == 200:
            try:
                r = response.json()
                count = 0
                price = 0
                for i in r['result']['items']:
                    count+=1
                    print(i['price'])
                    price += float(i['price'])

                print("Всего цен:", count)
                average_price = price/count
                my_price = average_price*0.95

                # срез до 2 знаков после запятой
                parts = str(average_price).split(".")  
                average_price = float(f"{parts[0]}.{parts[1][:2]}")

                parts = str(my_price).split(".")  
                my_price = float(f"{parts[0]}.{parts[1][:2]}")

                print("Средняя цена:", average_price)
                print("Наша цена:", my_price) #-5% от средней цены
                
                # Сохраняем в базу данных
                cursor.execute(
                    "INSERT INTO course (average_price, my_price, timestamp) VALUES (?, ?, ?)",
                    (average_price, my_price, datetime.now())
                )
                conn.commit()
                print("Сохранили") 
            except:
                print('Ошибка в запросе p2p цен')
                traceback.print_exc()

    except:
        print('Глобальная Ошибка в запросе p2p цен')
        traceback.print_exc()

    sleep(21600)