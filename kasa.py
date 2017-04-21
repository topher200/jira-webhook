import json

import requests

import config


OFF_STATE = "{\"system\":{\"set_relay_state\":{\"state\":0}}}"
ON_STATE = "{\"system\":{\"set_relay_state\":{\"state\":1}}}"
GET_SYS_INFO = "{\"system\":{\"get_sysinfo\":{}}}"


def lambda_handler(event, _):
    print("Received event: " + json.dumps(event, indent=2))

    if event['clickType'] == 'SINGLE':
        state = OFF_STATE
    if event['clickType'] == 'DOUBLE':
        state = ON_STATE

    url = 'https://%s/?token=%s' % (config.KASA_URL, config.KASA_TOKEN)
    payload = {
        'method': 'passthrough',
        'params': {
            'deviceId': config.KASA_DEVICE_ID,
            'requestData': state
        }
    }

    print('making request to %s with %s' % (url, payload))
    res = requests.post(url, json=payload)
    res.raise_for_status()

    print('response: "%s"' % res.json())
