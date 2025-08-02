import requests
from jwt_token_my import JWT_TOKEN

# Правильный базовый URL для API Точка Банка
base_url = "https://enter.tochka.com/uapi/open-banking/v1.0"

# Правильный эндпоинт для получения QR-кода СБП C2B
endpoint = "/sbp/c2b/qr/dynamic/get"  # Используем правильный путь согласно документации [[7]]

# Параметры для СБП C2B
params = {
    "type": "02",
    "bank": "100000000008",
    "sum": "5000",
    "cur": "RUB",
    "crc": "9C95"
}

headers = {
    'Authorization': f'Bearer {JWT_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Используем GET запрос для получения QR-кода СБП
response = requests.get(
    base_url + endpoint,
    params=params,
    headers=headers
)

print(response.status_code)
print(response.json())