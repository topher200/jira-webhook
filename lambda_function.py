import json

import requests

import config


print('Loading function')

API_HOST_URL = config.API_HOST_URL
API_ENDPOINT = config.API_ENDPOINT
API_REQUEST_URL = API_HOST_URL + API_ENDPOINT


def lambda_handler(event, _):
    # print("Received event: " + json.dumps(event, indent=2))

    key = json.loads(event['body'])['issue']['key']
    payload = {
        'issue_key': key
    }
    print('making request: %s' % payload)
    res = requests.put(API_REQUEST_URL, json=payload)
    if res.status_code == 200:
        print('Successfully updated "%s"' % key)
    else:
        print(
            'request failed. received response: %s. our payload: "%s"' %
            (res.status_code, payload)
        )

    return key
