import requests
import json
from django.core.mail import send_mail

def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulk"
    # message = "Hello users, This is a test message for OTP"

    querystring = {
                    "authorization":"t9Asnyb3NYqL8xU4VGrVej4T5RKRqbPUFKMIYIl3FCO15wcu8NaC8f1GOufU",
                    "sender_id":"FSTSMS",
                    "message":message,
                    "language":"english",
                    "route":"p",
                    "numbers":contactno
                  }

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = response.text
    d1 = json.loads(json_data)
    return d1['return']

def sendEmail(email,message):
    to = email
    subject = 'Test message'
    # message = message

    send_mail(subject, message, 'EMAIL_HOST_USER', [to])
    return email