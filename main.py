import hashlib
import sys
import argparse
import pyfiglet
from colorama import Fore
from colorama import init

init()
ascii_banner = pyfiglet.figlet_format("Password Cracker")
print(ascii_banner, end="")
print(Fore.MAGENTA + "Author:Vtechster\n")


def crackSha512(ohash, path):
    f = open(path, "r", encoding="utf8")
    for line in f.readlines():
        if hashlib.sha512(line.strip("\n").encode()).hexdigest() == ohash:
            print(Fore.GREEN + f"PASSWORD: {line}")
            return
    print(Fore.RED + "NOT FOUND")


def crackSha256(ohash, path):
    f = open(path, "r", encoding="utf8")
    for line in f.readlines():
        if hashlib.sha256(line.strip("\n").encode()).hexdigest() == ohash:
            print(Fore.GREEN + f"PASSWORD: {line}")
            return
    print(Fore.RED + "NOT FOUND")


def crackMd5(ohash, path):
    f = open(path, "r", encoding="utf8")
    for line in f.readlines():
        if hashlib.md5(line.strip("\n").encode()).hexdigest() == ohash:
            print(f"PASSWORD: {line}")
            return
    print(Fore.RED + "NOT FOUND")


def crackSha1(ohash, path):
    f = open(path, "r", encoding="utf8")
    for line in f.readlines():
        if hashlib.sha1(line.strip("\n").encode()).hexdigest() == ohash:
            print(Fore.GREEN + f"PASSWORD: {line}")
            return
    print(Fore.RED + "NOT FOUND")


def crackSha224(ohash, path):
    f = open(path, "r", encoding="utf8")
    for line in f.readlines():
        if hashlib.sha224(line.strip("\n").encode()).hexdigest() == ohash:
            print(Fore.GREEN + f"PASSWORD: {line}")
            return
    print(Fore.RED + "NOT FOUND")


def crackSha384(ohash, path):
    f = open(path, "r", encoding="utf8")
    for line in f.readlines():
        if hashlib.sha384(line.strip("\n").encode()).hexdigest() == ohash:
            print(Fore.GREEN + f"PASSWORD: {line}")
            return
    print(Fore.RED + "NOT FOUND")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode",
                        help="Specify hash type. Modes available are md5,sha256,sha512,sha1,sha224,sha384")
    parser.add_argument("-H", "--hash", help="Specify hash value")
    parser.add_argument("-w", "--wordlist", help="Specify wordlist path")
    args = parser.parse_args()

    ohash = args.hash
    path = args.wordlist
    mode = args.mode

    print("Hash Entered: ", ohash)
    if path is None or mode is None:
        print("No wordlist or hash type specified")
        exit()
    mode = mode.lower()
    print("Hash Type: ", mode)
    print("Wordlist: ", path)

    if mode == "sha256":
        crackSha256(ohash, path)
    elif mode == "sha512":
        crackSha512(ohash, path)
    elif mode == "md5":
        crackMd5(ohash, path)
    elif mode == "sha1":
        crackSha1(ohash, path)
    elif mode == "sha224":
        crackSha224(ohash, path)
    elif mode == "sha384":
        crackSha384(ohash, path)
    else:
        print("Unknown hash type")


if __name__ == "__main__":
    main()
