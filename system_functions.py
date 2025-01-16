import os
from time import sleep


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def sleep_and_clear(time):
    sleep(time)
    clear()