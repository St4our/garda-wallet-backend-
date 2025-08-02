import requests

cookies = {
    '_ym_uid': '1695728205883883946',
    '_ym_d': '1752657732',
    'carrotquest_device_guid': '026c2bb8-c7c2-44e1-95f4-20f638d85655',
    'carrotquest_uid': '2017877414842992692',
    'carrotquest_auth_token': 'user.2017877414842992692.50865-2f70e0b9a5f673ed7651e351f8.b2930adad2aa27c40548301f207e8df1ff20f006cb6b6db5',
    'spid': '1752657734605_2b2e7660d6a52526e77fa7f94953d513_1ktbsrcudqnk8h3b',
    'device_id': '328c1c7b-60c0-0070-dc9f-01d6bffd1682',
    'userName': '%D0%A1%D1%82%D0%B0%D0%BD%D0%B8%D1%81%D0%BB%D0%B0%D0%B2',
    'userId': 'fdc9f11e-55b6-42f1-a36e-d83b73e8e958',
    'tochka_analytics_client_uid': 'c3b95a83-1502-04a3-27b3-38d4d3b3b766',
    'hardware_metrics_client_uid': 'true',
    'tsr_analytics_client_uid': '7057c2fe-7b57-338d-46be-eaf586ba5ce2',
    'carrotquest_realtime_services_transport': 'wss',
    '_gcl_au': '1.1.1393253366.1753358422',
    'tmr_lvid': '8940d61767caadb20dec290766b2343f',
    'tmr_lvidTS': '1753358421916',
    'TochkaID': '0411970e-13d8-4345-bd6c-54d39e255b4f',
    'ID-CSRF-TOKEN': '34132114-64a9-4623-a63e-f4f70c0ad7da',
    'spsc': '1753775255493_f36f916d388fda90b8fc7578c509a68a_PA.cYbqAxEK52y5QqF70b.zLhStDvJJKX.DAYSwI5aoZ',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9',
    'baggage': 'sentry-environment=prod,sentry-release=microfront-root_app-prod%400.0.455-6b3733,sentry-public_key=b53f18cd6264e084b88f12d489f814e1,sentry-trace_id=bfb7fd7517ce49cfaf3b9dc821c24f33',
    'content-type': 'application/json',
    'origin': 'https://id.tochka.com',
    'priority': 'u=1, i',
    'referer': 'https://id.tochka.com/',
    'sec-ch-ua': '"Chromium";v="136", "YaBrowser";v="25.6", "Not.A/Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'bfb7fd7517ce49cfaf3b9dc821c24f33-8cb92d9527c9cfbc',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36',
    'x-client-time': '2025-07-29T13:05:07+05:00',
    'x-csrf-token': '34132114-64a9-4623-a63e-f4f70c0ad7da',
    'x-device-id': '328c1c7b-60c0-0070-dc9f-01d6bffd1682',
    'x-device-preferred-languages': 'ru, en',
    'x-kl-kis-ajax-request': 'Ajax_Request',
    'x-request-id': 'id.tochka.com-microfront-sso_auth-0.3.31-1e368455-692f-f67f-399e-bdfba5979ac3',
    'x-rpc-method': 'second_factor_auth',
    'x-screen-resolution': '360x740',
    'x-web-os': 'windows',
    'x-web-platform': 'desktop browser adaptive',
    # 'cookie': '_ym_uid=1695728205883883946; _ym_d=1752657732; carrotquest_device_guid=026c2bb8-c7c2-44e1-95f4-20f638d85655; carrotquest_uid=2017877414842992692; carrotquest_auth_token=user.2017877414842992692.50865-2f70e0b9a5f673ed7651e351f8.b2930adad2aa27c40548301f207e8df1ff20f006cb6b6db5; spid=1752657734605_2b2e7660d6a52526e77fa7f94953d513_1ktbsrcudqnk8h3b; device_id=328c1c7b-60c0-0070-dc9f-01d6bffd1682; userName=%D0%A1%D1%82%D0%B0%D0%BD%D0%B8%D1%81%D0%BB%D0%B0%D0%B2; userId=fdc9f11e-55b6-42f1-a36e-d83b73e8e958; tochka_analytics_client_uid=c3b95a83-1502-04a3-27b3-38d4d3b3b766; hardware_metrics_client_uid=true; tsr_analytics_client_uid=7057c2fe-7b57-338d-46be-eaf586ba5ce2; carrotquest_realtime_services_transport=wss; _gcl_au=1.1.1393253366.1753358422; tmr_lvid=8940d61767caadb20dec290766b2343f; tmr_lvidTS=1753358421916; TochkaID=0411970e-13d8-4345-bd6c-54d39e255b4f; ID-CSRF-TOKEN=34132114-64a9-4623-a63e-f4f70c0ad7da; spsc=1753775255493_f36f916d388fda90b8fc7578c509a68a_PA.cYbqAxEK52y5QqF70b.zLhStDvJJKX.DAYSwI5aoZ',
}

json_data = {
    'id': 'a0ddfb98-fee8-a6ce-8ef8-dfac5ae66879',
    'jsonrpc': '2.0',
    'method': 'second_factor_auth',
    'params': {
        'strict_sms': True,
        'auth_method': 'smsotp',
    },
}

response = requests.post(
    'https://id.tochka.com/api/v1/tochka-id/auth/v1/private',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

