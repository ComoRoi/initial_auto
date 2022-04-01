import requests
import json
import config

comConSet = config.COMMON_CONFIG

def post_message(channel, text): 
    SLACK_BOT_TOKEN = comConSet['oAuthToken']
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
        }
    payload = {
        'channel': channel,
        'text': text
        }
    r = requests.post('https://slack.com/api/chat.postMessage', 
        headers=headers, 
        data=json.dumps(payload)
        )

