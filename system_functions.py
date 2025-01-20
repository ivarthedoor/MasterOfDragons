import os
from time import sleep
import json


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def sleep_and_clear(time):
    sleep(time)
    clear()

def read_data():
    with open('questions.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data