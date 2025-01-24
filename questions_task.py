import random
from utils import sleep_and_clear, read_data

class QuestionsTask:
    def __init__(self):
        self.question = random.choice(read_data())
        if "answer" not in self.question or "description" not in self.question:
            raise ValueError("Invalid question format in data.")
        self.lenght = len(self.question["answer"])
        self.lifes = ["\U0001F534", "\U0001F534", "\U0001F7E0", "\U0001F7E0", "\U0001F7E0", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2"]
        self.used_letters = []
        self.password = ["_" for i in range(self.lenght)]

    def print_data(self):
        sleep_and_clear(1)
        print(f"Instruction: ?\n\n{"".join(self.lifes)}\n{self.question["description"]}\nUsed letters: {", ".join(self.used_letters)}\nAnswer: {"".join(self.password)}")


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
            elif not (user_input.isalpha() or user_input == " " or user_input == "?"):
                print("Letters only...")
                self.print_data()
            elif user_input == "?":
                print("1. Put one letter at once\n2. If your letter is correct it will show on board\n3. All used letters are shown in 'used letters' line\n4. Numbers are not allowed\n5. Be carefull, game distinguishes capitals and spaces\n6. Guess password until your lifes run out")
                sleep_and_clear(5)
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
        
# loop = QuestionsTask()
# loop.task_loop()