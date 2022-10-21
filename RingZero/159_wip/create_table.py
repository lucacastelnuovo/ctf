import hashlib, itertools


def create_table():
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

    tuples = itertools.product(alphabet, repeat=6)

    with open("table.txt", "w") as f:
        for tuple in tuples:
            password = "".join(tuple)
            hash = hashlib.sha1(password.encode()).hexdigest()

            line = f"{password} - {hash}\n"

            f.write(line)


def lookup_table(hash):
    with open("table.txt", "r") as f:
        line = next((l for l in f if hash in l), None)
        password = line.split(" - ")[0].strip()
        print(password)
        exit()


lookup_table("ce39f3667ebb5f8275cd39c541f2dd8bbf8e7854")
