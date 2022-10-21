#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/13

import hashlib, requests

# First we get the message page
html = requests.get("http://challenges.ringzer0team.com:10013/").text

# After that we extract the message from the html string
message = html.split("-----<br />")[1].split("<br />")[0].strip()

# Then we hash the message with sha512
hash = hashlib.sha512(message.encode()).hexdigest()

# Next we send the hash to the server
response = requests.post("http://challenges.ringzer0team.com:10013/?r=" + hash).text

# Finally we extract the flag from the response html
flag = response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()

print(flag)
