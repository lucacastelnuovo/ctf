#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/57

"""
    This is a brute-force challenge, a bit more complex than challenge 56.

    First I analysed the hash with https://www.tunnelsup.com/hash-analyzer and found out that it was a SHA1 hash. Assuming that the answer was once again between 0 and 9999 like in challenge 56 I wrote a script that brute-forces the hash (including the salt) and submits the result to the server. The script is shown below.
"""

import hashlib, requests


def get_input():
    # Get challenge html
    html = requests.get("http://challenges.ringzer0team.com:10057/").text

    hash = html.split("----- BEGIN HASH -----<br />")[1].split("<br />")[0].strip()
    salt = html.split("----- BEGIN SALT -----<br />")[1].split("<br />")[0].strip()

    return [hash, salt]


def submit_result(i):
    # Send the result to the server
    response = requests.post(
        "http://challenges.ringzer0team.com:10057/?r=" + str(i)
    ).text

    # Extract the flag from the response html
    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def main():
    [hash, salt] = get_input()

    # Brute force the hash
    for i in range(9999):
        input = str(i) + "" + salt

        validate = hashlib.sha1(input.encode()).hexdigest()
        match = hash == validate

        # Output progress for extra fun
        print(input + " " + validate)

        if match:
            submit_result(i)

    print("\nHash could not be cracked!")


if __name__ == "__main__":
    main()
