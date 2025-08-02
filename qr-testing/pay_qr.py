import requests
from jwt_token_my import JWT_TOKEN

headers = {
    'Authorization': f'Bearer {JWT_TOKEN}',
}
#https://qr.nspk.ru/AD200020167JNNOQ90COF8ER261DN0MR?type=02&bank=100000000008&sum=5000&cur=RUB&crc=9C95
response = requests.post(
    "https://i.tochka.com/bank/payments/m/sbp_c2b/AD200020167JNNOQ90COF8ER261DN0MR",
    headers=headers,
)

print(response.status_code)
print(response.text)