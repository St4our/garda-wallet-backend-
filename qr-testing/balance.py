import requests
from jwt_token_my import JWT_TOKEN

headers = {
    'Authorization': f'Bearer {JWT_TOKEN}',
}

response = requests.get(
    'https://enter.tochka.com/uapi/open-banking/v1.0/accounts/40802810320000189461/044525104/balances', # №счета и Бик
    headers=headers,
)

print(response.status_code)
print(response.text)