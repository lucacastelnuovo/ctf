#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/17

"""
    Insert explanation here
"""

import requests
import base64

CHALLENGE_PORT = 10017


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/").text

    img = html.split("data:image/png;base64,")[1].split('"')[0].strip()

    return [img]


def submit_result(result):
    # Send the result to the server
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/?r=" + str(result)
    ).text

    # Extract the flag from the response html
    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def save_image():
    [img] = get_input()

    with open("image.png", "wb") as fh:
        fh.write(base64.decodebytes(img.encode()))

    fh.close()


def main():
    save_image()


if __name__ == "__main__":
    main()
