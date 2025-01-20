from player import PlayerData
from system_functions import sleep_and_clear

class InitializeGame(PlayerData):
    def __init__(self):
        self.player = PlayerData()

    def run_the_game(self):
        print(f"    Welcome Wanderer...\n \
    You shall fear, for I am a ghost of Ancalacan, fear of the east...\n \
    The greatest of all dragons...\n \
    You dare to attempt to my temple!\n \
    Who are you?! And What is your name?!")
        sleep_and_clear(3)
        self.player.initialize_player()
        sleep_and_clear(3)
        print(f"Welcome {self.player.nick}, the {self.player.type}\n \
              what do you seek in my home...")

# Tworzenie instancji i uruchamianie gry
run = InitializeGame()
run.run_the_game()
