import hashlib, itertools

LENGTH = 6


def create_table():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    half_alphabet = alfabet[: len(alfabet) // 2]

    tuples = itertools.product(alfabet, repeat=LENGTH)

    with open("table.txt", "w") as f:
        for tuple in tuples:
            # Only create half a table, to compensate run the solver multiple times
            if not tuple[0] in half_alphabet:
                continue

            password = "".join(tuple)
            hash = hashlib.sha1(password.encode()).hexdigest()

            line = f"{hash} - {password}\n"

            f.write(line)


if __name__ == "__main__":
    create_table()
