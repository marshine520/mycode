#!/usr/bin/python3
# -*- coding: utf-8 -*-
from twilio.rest import Client

account_sid = "AC016ee3b3cbf42de38c2c6c6804bb6056"
auth_token = "315b9a5920cd3e60c6345730971a95a8"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8618942061726",    # 区号+你的手机号码   
    from_="+8618942061726",   # 你的 twilio 电话号码
    body="Do you know who I am ?"
)
print(message.sid)