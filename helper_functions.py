import platform
import os
import subprocess


def peek(filePath, n=10, l=80):
    """Shows the first n lines of a file with a maximum of l columns"""
    with open(filePath, encoding="utf8", errors="replace") as file:
        for i, line in enumerate(file):
            if i > n:
                print("...")
                break
            print(line.rstrip()[0:l], end="")
            if len(line) > l:
                print(" ...", end="")
            print("")


def explorer_open(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    else:
        if platform.system() == "Darwin":
            subprocess.call("open", file_path)
        else:
            subprocess.call("xdg-open", file_path)
