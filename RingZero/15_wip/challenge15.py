#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/15

"""
    This is a brute-force challenge, a bit more complex than challenge 56.

    First I analysed the hash with https://www.tunnelsup.com/hash-analyzer and found out that it was a SHA1 hash. Assuming that the answer was once again between 0 and 9999 like in challenge 56 I wrote a script that brute-forces the hash (including the salt) and submits the result to the server. The script is shown below.
"""

import requests, hashlib

CHALLENGE = 15


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:100{CHALLENGE}/").text

    elf = (
        html.split("----- BEGIN Elf Message -----<br />")[1].split("<br />")[0].strip()
    )
    checksum = (
        html.split("----- BEGIN Checksum -----<br />")[1].split("<br />")[0].strip()
    )

    return [elf, checksum]


def submit_result(result):
    # Send the result to the server
    response = requests.post(
        f"http://challenges.ringzer0team.com:100{CHALLENGE}/?r=" + str(result)
    ).text

    # Extract the flag from the response html
    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def main():
    [elf, checksum] = get_input()

    print(elf)
    # print(checksum)

    result = "yeet"
    # submit_result(result)


if __name__ == "__main__":
    main()
