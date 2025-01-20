class PlayersChoices:
    def __init__(self):
        self.first_d_choice = {1: "Wisdom", 2: "Power", 3: "Kill a dragon"}

    def get_choice(self, prompt, choices):
        while True:
            try:
                choice = int(input(prompt))
                if choice in choices:
                    return choice
                print(f"Input only: {', '.join(map(str, choices))}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def initialize_choice(self):
        self.first_dialog_choice = self.first_d_choice[self.get_choice("1. I seek for wisdom\n2. I seek for power\n3. I'm here to destroy you\n", self.first_d_choice.keys())]


