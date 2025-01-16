import json
import random

with open('questions.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)


question = random.choice(data)
# word = "czarodziej"
lenght = len(question["answer"])
lifes = ["\U0001F534", "\U0001F534", "\U0001F7E0", "\U0001F7E0", "\U0001F7E0", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2"]
wrong_letters = []
password = ["_" for i in range(lenght)]



def print_data():
    print("".join(lifes))
    print(question["description"])
    print(f"użyte litery: {", ".join(wrong_letters)}")
    print(f"nazwa: {"".join(password)}")

print("".join(lifes))
print(question["description"])
print(f"użyte litery: {", ".join(wrong_letters)}")
print(f"nazwa: {"".join(password)}")

while "_" in  password and len(lifes) >= 1:
    user_input = input("Podaj literę: ")
    if len(user_input) > 1:
        print("max 1 litera...")
        print_data()
    elif user_input in  wrong_letters:
        print("było...")
        lifes.pop()
        print_data()
    elif not (user_input.isalpha() or user_input == " "):
        print("Tylko litery...")
        print_data()
    else:
        if user_input in question["answer"]:
            for x in range(lenght):
                if question["answer"][x] == user_input:
                    password[x] = user_input
            print_data()
        elif user_input not in question["answer"]:
            wrong_letters.append(user_input)
            lifes.pop()
            print_data()
        
