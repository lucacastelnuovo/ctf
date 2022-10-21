#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/56

"""
    This is a brute-force challenge.

    First I analysed the hash with https://www.tunnelsup.com/hash-analyzer and found out that it was a SHA1 hash. Then I cracked the hash with https://crackstation.net/ and found out that the hash was a number between 0 and 9999. This gave me the information that the answer is a 4 digit number that is hashed with sha1.

    Next I wrote a script that brute-forces the hash and submits the result to the server. The script is shown below.
"""

import hashlib, requests


def get_hash():
    # Get challenge html
    html = requests.get("http://challenges.ringzer0team.com:10056/").text

    # Extract hash from html
    return html.split("-----<br />")[1].split("<br />")[0].strip()


def submit_result(i):
    # Send the result to the server
    response = requests.post(
        "http://challenges.ringzer0team.com:10056/?r=" + str(i)
    ).text

    # Extract the flag from the response html
    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def main():
    hash = get_hash()

    # Brute force the hash
    for i in range(9999):
        validate = hashlib.sha1(str(i).encode()).hexdigest()
        match = hash == validate

        # Output progress for extra fun
        print(str(i) + " " + validate)

        if match:
            submit_result(i)

    print("\nHash could not be cracked!")


if __name__ == "__main__":
    main()
