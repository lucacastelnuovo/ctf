#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/15
# Hint: ELF is a Linux executable file where the strings are stored.

import requests, re, base64, subprocess

CHALLENGE_PORT = 10015


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/").text

    elf = (
        html.split("----- BEGIN Elf Message -----<br />")[1].split("<br />")[0].strip()
    )
    checksum = (
        html.split("----- BEGIN Checksum -----<br />")[1].split("<br />")[0].strip()
    )

    return [elf, checksum]


def submit_result(result):
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/?r=" + str(result)
    ).text

    try:
        flag = (
            response.split('<div class="alert alert-info">')[1]
            .split("</div>")[0]
            .strip()
        )

        print("\n" + flag)
        exit()
    except:
        print(response)
        pass


def base64Decode(input):
    return base64.b64decode(input).decode("utf-8")


def main():
    [elf, _] = get_input()

    with open("./elf.txt", "w") as f:
        f.write(elf)

    subprocess.call(["node", "solution.js"])

    output = subprocess.check_output(["./elf.bin"])
    output = output.decode("utf-8")

    if output:
        submit_result(output)

    print("Error: No output")

    ######################

    # Decode base64 payload variable number of times
    # try:
    #     while True:
    #         elf = base64Decode(elf)
    # except:
    #     pass

    # elf = bytearray(elf, "utf-8")

    # elf = Buffer.from(elf, "binary")

    # Reverse string
    # JS: elf = elf.reverse();
    # elf = elf[::-1]

    # payload = "./elf2.bin"

    # Write payload to file
    # with open(payload, "wb") as f:
    #     f.write(elf)

    # Execute payload and get output
    # output = subprocess.check_output([payload])
    # output = output.decode("utf-8")

    # Submit result
    # print(output)


if __name__ == "__main__":
    main()
