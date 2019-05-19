##################################################
# v3 Mail Send #
# POST /mail/send #
# This endpoint has a helper, check it out
# [here](https://github.com/sendgrid/sendgrid-python/blob/master/use_cases/README.md).

import sendgrid
import base64
import json
import os


with open('/home/tiantian/Crawler/CrawBriefing.html', 'r') as f:
    html = f.read()
with open('/home/tiantian/Crawler/Cache/BaiduStockInfo.txt', 'rb') as f:
    b_data = f.read()

data = {
    "attachments": [
        {
            "content": base64.b64encode(b_data).decode(),
            "content_id": "ID 1",
            "disposition": "attachment",
            "filename": "BaiduStockInfo.txt",
            "name": "BaiduStockInfo",
            "type": "text/plain"
        }
    ],
    "content": [
        {
            "type": "text/html",
            "value": html
        }
    ],
    "from": {
        "email": 'from@email.com',
        "name": "Wang Tiantian"
    },
    "personalizations": [
        {
            "subject": 'Crawler Briefing: Stock Infomation from Baidu Stock',
            "to": [
                {
                    "email": "target@email.com"
                }
            ]
        }
    ]
}

try:
    sg = sendgrid.SendGridAPIClient('SEND_GRID_KEYS')
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

