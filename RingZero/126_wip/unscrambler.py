# Original Version: https://github.com/tinmarr/Word-Unscrambler/blob/master/LICENSE


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


word = input("Enter scrambbled word: ")
print(unscramble(word))
