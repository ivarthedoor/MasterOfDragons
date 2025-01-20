class PlayerData:
    def __init__(self):
        self.gender = "Male" if self.get_choice("Input your gender:\n1. Male\n2. Female\n", [1, 2]) == 1 else "Female"
        self.nick = input("Give me your name...: ")
        self.races = {1: "Man", 2: "Elf", 3: "Dwarf", 4: "Orc"}
        self.type = self.races[self.get_choice("What's your race?\n1. Man\n2. Elf\n3. Dwarf\n4. Orc\n", self.races.keys())]
        self.final_player_data = {"Gender": self.gender, "Nick": self.nick, "Race": self.type}

    def get_choice(self, prompt, choices):
        while True:
            try:
                choice = int(input(prompt))
                if choice in choices:
                    return choice
                print(f"Input only: {', '.join(map(str, choices))}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_data(self):
        for key, value in self.final_player_data.items():
            print(f"{key}: {value}")

print_player = PlayerData()
print_player.display_data()