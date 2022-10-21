# TODO: build binary search

def search_table(hash):
    with open("table.txt", "r") as f:
        line = next((l for l in f if hash in l), None)

        if line:
            print(line[-6 - 1 :])
            exit()


if __name__ == "__main__":
    hash = ""
    search_table(hash)

    print("No match found in table.txt" + hash)
