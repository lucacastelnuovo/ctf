#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/14

import hashlib, requests

# First we get the message page
html = requests.get("http://challenges.ringzer0team.com:10014/").text

# After that we extract the binary from the html string
binary = html.split("-----<br />")[1].split("<br />")[0].strip()

# Next we convert the binary to a string
message = "".join(
    chr(int(binary[i * 8 : i * 8 + 8], 2)) for i in range(len(binary) // 8)
)

# Then we hash the message with sha512
hash = hashlib.sha512(message.encode()).hexdigest()

# Next we send the hash to the server
response = requests.post("http://challenges.ringzer0team.com:10014/?r=" + hash).text

# Finally we extract the flag from the response html
flag = response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()

print(flag)
