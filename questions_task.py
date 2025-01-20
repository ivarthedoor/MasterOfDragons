import json
import random
from system_functions import sleep_and_clear, read_data

class QuestionsTask:
    def __init__(self):
        self.question = random.choice(read_data())
        self.lenght = len(self.question["answer"])
        self.lifes = ["\U0001F534", "\U0001F534", "\U0001F7E0", "\U0001F7E0", "\U0001F7E0", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2"]
        self.used_letters = []
        self.password = ["_" for i in range(self.lenght)]

    def print_data(self):
        sleep_and_clear(1)
        print("".join(self.lifes))
        print(self.question["description"])
        print(f"Used letters: {", ".join(self.used_letters)}")
        print(f"Answer: {"".join(self.password)}")

    def task_loop(self):
        self.print_data()
        while "_" in  self.password and len(self.lifes) > 0:
            user_input = input("Put your letter: ")
            if len(user_input) > 1:
                print("max 1 letter...")
                self.print_data()
            elif user_input in  self.used_letters:
                print("You used that letter already...")
                self.lifes.pop()
                self.print_data()
            elif not (user_input.isalpha() or user_input == " "):
                print("Letters only...")
                self.print_data()
            else:
                if user_input in self.question["answer"]:
                    for x in range(self.lenght):
                        if self.question["answer"][x] == user_input:
                            self.password[x] = user_input
                            self.used_letters.append(user_input)
                    self.print_data()
                elif user_input not in self.question["answer"]:
                    self.used_letters.append(user_input)
                    self.lifes.pop()
                    self.print_data()

            if len(self.lifes) == 0:
                print(f"You lost, answer is: {self.question["answer"]}")
                sleep_and_clear(5)
                break
            if "_" not in self.password:
                print("Correct!")
                sleep_and_clear(5)
        
loop = QuestionsTask()
loop.task_loop()