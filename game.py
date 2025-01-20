from player import PlayerData
from players_choices import PlayersChoices
from system_functions import sleep_and_clear

class InitializeGame(PlayerData):
    def __init__(self):
        self.player = PlayerData()
        self.choices = PlayersChoices()

    def run_the_game(self):
        print(f"    Welcome Wanderer...\n \
    You shall fear, for I am a ghost of Ancalacan, fear of the east...\n \
    The greatest of all dragons...\n \
    You dare to attempt to my temple!\n \
    Who are you?! And What is your name?!")
        sleep_and_clear(1)
        self.player.initialize_player()
        sleep_and_clear(1)
        print(f"Welcome {self.player.nick}, the {self.player.type}\nwhat do you seek in my home...")
        self.choices.initialize_first_choice()

        if self.choices.first_dialog_choice == 1:
            print("STH ABOUT WISDOM")
        elif self.choices.first_dialog_choice == 2:
            print("POWER DIALOG")
        else:
            print("STH BOUT KILLING")

# Tworzenie instancji i uruchamianie gry
run = InitializeGame()
run.run_the_game()
