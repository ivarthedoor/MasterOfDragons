from player import PlayerData
from players_choices import PlayersChoices
from questions_task import QuestionsTask
from loot import BodyLoot
from system_functions import sleep_and_clear, sleep

class InitializeGame(PlayerData):
    def __init__(self):
        # self.player = PlayerData()
        self.choices = PlayersChoices()
        self.loot = BodyLoot()
        self.question = QuestionsTask()
        super().__init__()

    def run_the_game(self):
        print(f"    Ancalacan: Welcome Wanderer...\n \
        You shall fear, for I am a ghost of Ancalacan, fear of the east...\n \
        The greatest of all dragons...\n \
        You dare to attempt to my temple!\n \
        Who are you?! And What is your name?!")
        sleep_and_clear(20)
        self.initialize_player()
        sleep_and_clear(1)
        print(f"Ancalacan: Welcome {self.nick}, the {self.type}\n   what do you seek in my home...")
        self.choices.initialize_first_choice()
        self.interface()
        print("You enter through ancient stone door, to an old, ruined hall.\n \
        walls and roof are full of holes, aeverything is covered in moss. You feel the smell of water and rot.\n \
        You make few steps inside and right after you enter the room, something hits you from the back!")
        sleep_and_clear(20)
        self.interface()
        print("...")
        sleep_and_clear(5)
        self.interface()
        print("Goblin: ghrghnhthnhmrht")
        sleep_and_clear(5)
        self.interface()
        print("You wake up, beeing dragged by leg, by stinking, ugly, little creature.\n \
        You use other leg to kick goblin in the back!\n \
        Right after hit, he drops your leg and falls.\n \
        In one quick swing of your sword you kill the beast.")
        sleep_and_clear(20)
        self.loot.goblin_loot()
        sleep_and_clear(10)
        

run = InitializeGame()
run.run_the_game()
















# self.question.task_loop()
