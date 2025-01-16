word = "czarodziej"
lenght = len(word)
lifes = ["\U0001F534", "\U0001F534", "\U0001F7E0", "\U0001F7E0", "\U0001F7E0", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2"]
wrong_letters = []
password = ["_" for i in range(lenght)]



def print_data():
    print("".join(lifes))
    print(f"użyte litery: {", ".join(wrong_letters)}")
    print(f"nazwa: {"".join(password)}")

print("".join(lifes))
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
        if user_input in word:
            for x in range(lenght):
                if word[x] == user_input:
                    password[x] = user_input
            print_data()
        elif user_input not in word:
            wrong_letters.append(user_input)
            lifes.pop()
            print_data()
        
