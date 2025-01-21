from player import PlayerData
from players_choices import PlayersChoices
from system_functions import sleep_and_clear

class InitializeGame(PlayerData):
    def __init__(self):
        self.player = PlayerData()
        self.choices = PlayersChoices()

    def first_dialog(self):
        if self.choices.first_dialog_choice == "Wisdom":
            print("You seek wisdom... A wise decision, young one.\nDifficult path lays ahead, first you must prove, you are worthy of my knowledge.")
            sleep_and_clear(10)
            print("To prove that, you will have to overcome all challenges I will put on you.")
            sleep_and_clear(10)
        elif self.choices.first_dialog_choice == "Power":
            print("You seek power... Many have fallen to that temptation.\nYet only few gained enough power to reach the end of the path.")
            sleep_and_clear(10)
            print("We shall see if you are worthy of power of a dragon!")
            sleep_and_clear(10)
        elif self.choices.first_dialog_choice == "Kill a dragon":
            print("You wish to destroy... There is a dark path ahead.\nAs dark as your soul might mecome if you will continue this path.\nThink wisely, hard task is before you... harder than you can imagine...")
            sleep_and_clear(10)
            print("If you wish to kill me, you will have to reach me first Hahahahahaha!")
            sleep_and_clear(10)

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
        self.first_dialog()


        

# Tworzenie instancji i uruchamianie gry
run = InitializeGame()
run.run_the_game()
