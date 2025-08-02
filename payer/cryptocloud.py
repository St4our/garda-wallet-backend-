# API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiTmpVME5UYz0iLCJ0eXBlIjoicHJvamVjdCIsInYiOiI1OTBjN2VhMzU3ODkzZWQzZDA0YmIwNjM3NmI5NjExYmM5ZjQ2MGMyYmVjNDIyYWQ4MGFmYzVlYzRkYTcxOTM5IiwiZXhwIjo4ODE1Mzc5NTYwOX0.oEfcUTDooROql0b4QV2l9fDAxtzN0NhM5tf4WgJlwsE"
# SHOP_ID = "h4VbLcBkprLdfhlv"
# SECRET_KEY = "Iu3XFyai4H6jK5d2caLWB1brOKVTM1ddLGcv"

import requests
# import os

# API_KEY = os.environ.get('API_KEY')
# SHOP_ID = os.environ.get('SHOP_ID')
# SECRET_KEY = os.environ.get('SECRET_KEY')

def create_invoce(API_KEY, SHOP_ID, amount, cryptocurrency):
    url = "https://api.cryptocloud.plus/v2/invoice/create"
    headers = {
        "Authorization": f"Token {API_KEY}"
    }

    json = {
        "shop_id": SHOP_ID,
        "amount": amount,
        # "order_id": order_id, #Произвольный номер счета во внешней системе
        # "email": email, #Email адрес плательщика
        "add_fields": {
            "available_currencies": ["USDT_TRC20"," USDT_ERC20", "USDT_TON"],
            "cryptocurrency": cryptocurrency #"USDT_TRC20"
            }#Дополнительные параметры
    }

    response = requests.post(url, headers=headers, json=json)

    if response.status_code == 200:
        print("Success:", response.json())
        return response.json()
    else:
        print("Fail:", response.status_code, response.text)
        return {"status": "Failed", 'status_code': response.status_code, "more": response.text}
    


#Информация о счете
def check_invoce(uuids):
    url = "https://api.cryptocloud.plus/v2/invoice/merchant/info"
    headers = {
        "Authorization": f"Token {API_KEY}"
    }

    json = {
        "uuids": uuids #идентификатор счетов   INV номер
        }
    
    response = requests.post(url, headers=headers, json=json)

    if response.status_code == 200:
        print("Success:", response.json())
        return response.json()
    else:
        print("Fail:", response.status_code, response.text)
        return {"status": "Failed", 'status_code': response.status_code, "more": response.text}


# amount = 105
# cryptocurrency = "USDT_TRC20"
# create_invoce(amount, cryptocurrency)

# uuids = "INV-D0TH26T6"
# check_invoce(uuids)