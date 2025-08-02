import requests

cookies = {
    'tochka_analytics_client_uid': '42fcf827-e94a-83f3-df29-893aa396bb51',
    'carrotquest_session': 'x2pw7y8ai9albcwg6m7bg5s86hoy7yqa',
    '_ym_uid': '1753429139960938999',
    '_ym_d': '1753429139',
    '_ym_isad': '2',
    'carrotquest_session_started': '1',
    'carrotquest_device_guid': 'd12f7ddb-0e23-4aa6-980a-6ff5d5bfa6ed',
    'carrotquest_uid': '2024348443425638847',
    'carrotquest_auth_token': 'user.2024348443',
    '_ym_visorc': 'b',
    '_gcl_au': '1.1.19',
    'tmr_lvid': '57d25a9ecb',
    'tmr_lvidTS': '1753429140814',
    '_ga': 'GA1.2.59602250.1753429141',
    '_gid': 'GA1.2.1139062738.1753429141',
    'carrotquest_realtime_services_transport': 'wss',
    'spid': '1753429141',
    'device_id': 'cbab9',
    'tsr_analytics_client_uid': 'be2f4d43',
    'RsRememberMeToken': 'd3547af1-35f9-411f-9dc5-9865f71bb7f0',
    'X-CSRF-TOKEN': 'dab26a95-943a-47',
    'SP_TOKEN': '79ee65f2ff4644a1864',
    'SP_THUMBPRINT': '68d6c4cd15de3f6',
    'hardware_metrics_client_uid': 'true',
    'spsc': '1753429285500_c863501d0bca8d3682028a9b1',
    'JSESSIONID': 'DDFE931F1E73B5EFC205DCA6A5A3E510',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://i.tochka.com',
    'priority': 'u=4, i',
    'referer': 'https://i.tochka.com/bank/payments/m/sbp_c2b/AD20005QIJJGTPMU8NAR1P86MDNPU9OU',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

data = '{"events":[{"url":"https://i.tochka.com/bank/payments/m/sbp_c2b/AD20005QIJJGTPMU8NAR1P86MDNPU9OU","dateTime":"2025-07-25T07:46:48.764Z","action":"click","params":{"target":"sbp-qr/send-btn","elements":["sbp-qr/send-btn","sbp-qr/send-btn/wrapper/clipPath","sbp-qr/send-btn/wrapper/shadow","sbp-qr/send-btn/wrapper","Footer/containerChildren","Footer","sbp-qr/main-page/footer","sbp-qr/main-page/innerBody","css-1bzzrwd-sciLayout-inner---size-l","sbp-qr/main-page/outerWrapper","ScrollableViewSimpleBar/content","sbp-qr/main-page/outerBody","css-11b8glx-sciLayoutWrapper---with-header","FocusManager","sbp-qr/main-page","ptr-wrapper","core-module-modal-route-dialog/wrapper","core-module-modal-route-dialog"],"text":"Оплатить","pageX":285,"pageY":883,"screenX":474,"screenY":754},"sequenceNumber":"11","resolution":"375x667","windowSize":"375x667","customerCode":"304030445"}],"context":{"customerCode":"304030445","mainCustomerCode":"304036882","sessionCreated":"2025-07-25T07:40:23.923Z","userId":"fdc9f11e-55b6-42f1-a36e-d83b73e8e958","sessionId":"d17e67db","clientUid":"be2f4d43-1b20-2aab-24a9-96e3922bb20b","manualAnalyticsClientUid":"42fcf827-e94a-83f3-df29-893aa396bb51","siteId":"71"}}'.encode()

response = requests.post('https://i.tochka.com/api/v1/eventon/v1/analytics/web_batch', cookies=cookies, headers=headers, data=data)