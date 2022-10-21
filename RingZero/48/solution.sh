#!/bin/sh

# User : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/48

curl -X PUT 'https://ringzer0ctf.com/challenges/48' \
-H 'Cookie: PHPSESSID=REDACTED' \
  --compressed | grep -i flag
