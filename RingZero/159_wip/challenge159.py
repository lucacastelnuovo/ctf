#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/159

import requests, hashlib, itertools

CHALLENGE_PORT = 10159


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/").text

    hash = html.split("----- BEGIN HASH -----<br />")[1].split("<br />")[0].strip()

    return [hash]


def submit_result(result):
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/?r=" + str(result)
    ).text

    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def lookup_table(hash):
    with open("table.txt", "r") as f:
        line = next((l for l in f if hash in l), None)
        password = line.split(" - ")[0].strip()

        if password:
            print(password)
            exit()


def main():
    [hash] = get_input()

    lookup_table(hash)

    print("No match found in table.txt" + hash)


if __name__ == "__main__":
    main()
