#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/121

"""
    Insert explanation here
"""

import requests
import ctypes, mmap

CHALLENGE_PORT = 10121


def get_input():
    html = requests.get(f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/").text

    shellcode = (
        html.split("----- BEGIN SHELLCODE -----<br />")[1].split("<br />")[0].strip()
    )

    return [shellcode]


def submit_result(result):
    # Send the result to the server
    response = requests.post(
        f"http://challenges.ringzer0team.com:{CHALLENGE_PORT}/?r=" + str(result)
    ).text

    # Extract the flag from the response html
    flag = (
        response.split('<div class="alert alert-info">')[1].split("</div>")[0].strip()
    )

    print("\n" + flag)
    exit()


def main():
    [shellcode] = get_input()

    # Allocate an executable memory and write shellcode to it
    mem = mmap.mmap(
        -1,
        mmap.PAGESIZE,
        mmap.MAP_SHARED,
        mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC,
    )

    mem.write(shellcode.encode())

    # Get actuall mmap address (I don't know the proper way to get the address sorry...), Assuming x64
    addr = int.from_bytes(ctypes.string_at(id(mem) + 16, 8), "little")
    print(hex(addr))

    # Create the function
    functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
    fn = functype(addr)

    # Run shellcode
    fn()


if __name__ == "__main__":
    main()
