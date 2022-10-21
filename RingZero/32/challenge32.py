#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/32

import requests

# First we get the message page
html = requests.get("http://challenges.ringzer0team.com:10032/").text

# After that we extract the formula from the html string
formula = html.split("-----<br />")[1].split(" = ?")[0].strip()

# We split the formula into parts
numbers = formula.split(" ")

# Next we calculate the result of the parts while converting them to the same base
result = int(numbers[0]) + int(numbers[2], 16) - int(numbers[4], 2)

# Then we send the result to the server
response = requests.post(
    "http://challenges.ringzer0team.com:10032/?r=" + str(result)
).text

# Finally we extract the flag from the response html
flag = response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()

print(flag)
