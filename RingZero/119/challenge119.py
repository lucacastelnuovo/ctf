#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/119

import requests

CHALLENGE_PORT = 10119


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/").text

    msg = (
        html.split("----- BEGIN MESSAGE -----<br />")[1]
        .split("----- END MESSAGE -----")[0]
        .strip()
    )

    return [msg]


def submit_result(result):
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/?r=" + str(result)
    ).text

    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def main():
    [msg] = get_input()
    msg = msg.replace("&nbsp;", "_").replace("x", "#").replace("<br />", "\n").strip()

    number_0 = "_###_\n#___#\n#___#\n#___#\n_###_"
    number_1 = "_##__\n#_#__\n__#__\n__#__\n#####"
    number_2 = "_###_\n#___#_\n__##_\n_#___\n#####"
    number_3 = "_###_\n#___#\n__##_\n#___#\n_###_"
    number_4 = "_#___#\n#____#\n_#####\n_____#\n____#"
    number_5 = "#####\n#____\n_####\n____#\n#####"

    msg = msg.replace(number_0, "0")
    msg = msg.replace(number_1, "1")
    msg = msg.replace(number_2, "2")
    msg = msg.replace(number_3, "3")
    msg = msg.replace(number_4, "4")
    msg = msg.replace(number_5, "5")

    msg = msg.replace("\n", "")

    submit_result(msg)


if __name__ == "__main__":
    main()
