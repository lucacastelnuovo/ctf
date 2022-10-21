#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/126

import requests

CHALLENGE_PORT = 10126


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/").text

    words = html.split("----- BEGIN WORDS -----<br />")[1].split("<br />")[0].strip()

    return [words]


def submit_result(result):
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/?r=" + str(result)
    ).text

    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


# Original Version: https://github.com/tinmarr/Word-Unscrambler/
def wordToVector(word):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    vector = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

    word = word.lower()
    word_list = list(word)

    for i in range(0, len(word_list)):
        if word_list[i] in alphabet:
            index = alphabet.index(word_list[i])
            vector[index] += 1

    return vector


def vectorToInt(vector):
    pv = 0
    f = 0

    for i in range(0, len(vector)):
        wip = vector[i] * (2**pv)
        f += wip
        pv += 4

    return f


def getDictionary():
    file = open("dictionary.txt", "r")
    dictionary = file.read()
    file.close()

    return dictionary.split("\n")


def parseDictionary():
    dictionary = getDictionary()

    parsedDictionary = {}

    for i in range(0, len(dictionary)):
        vector = wordToVector(dictionary[i])
        Int = vectorToInt(vector)

        if Int in parsedDictionary:
            tat = parsedDictionary.get(Int)
            tat.append(dictionary[i])

            parsedDictionary[Int] = tat

        elif Int not in parsedDictionary:
            parsedDictionary[Int] = [dictionary[i]]

    return parsedDictionary


def unscramble(word):
    vector = wordToVector(word)
    vectorInt = vectorToInt(vector)
    parsedDictionary = parseDictionary()
    result = parsedDictionary.get(vectorInt, [False])

    return result[0] or "Word not found!"


def main():
    # [words] = get_input()
    words = "drummers,underwriter,syncopes,demineralized,tuscltaioraayln,arlmbeiefrro,churchless"

    words = words.split(",")

    for word in words:
        word = unscramble(word)

    words = ",".join(words)

    print(words)


if __name__ == "__main__":
    main()
