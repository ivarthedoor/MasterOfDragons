from player import PlayerData
from players_choices import PlayersChoices
from questions_task import QuestionsTask
from loot import BodyLoot
from utils import sleep_and_clear, sleep

class InitializeGame(PlayerData):
    def __init__(self):
        self.health = 100
        self.damage = 10
        self.choices = PlayersChoices()
        self.loot = BodyLoot()
        self.question = QuestionsTask()
        super().__init__()

    def interface(self):
        self.health += self.loot.add_health_points
        self.health += self.question.punish_points
        self.damage += self.loot.add_damage_points
        self.loot.add_health_points = 0
        self.loot.add_damage_points = 0
        self.question.punish_points = 0
        print(f"❤️: {self.health}\n🗡️: {self.damage}\n")



    def run_the_game(self):
    #     print(f"    Ancalacan: Welcome Wanderer...\n \
    # You shall fear, for I am a ghost of Ancalacan, fear of the east...\n \
    # The greatest of all dragons...\n \
    # You dare to attempt to my temple!\n \
    # Who are you?! And What is your name?!")
    #     sleep_and_clear(16)
    #     self.initialize_player()
    #     sleep_and_clear(1)

    #     print(f"Ancalacan: Welcome {self.name}, the {self.type}\n   what do you seek in my home...")
    #     self.choices.first_choice()
    #     self.interface()

    #     print("You enter through ancient stone door, to an old, ruined hall.\n \
    # walls and roof are full of holes, aeverything is covered in moss. You feel the smell of water and rot.\n \
    # You make few steps inside and right after you enter the room, something hits you from the back!")
    #     sleep_and_clear(16)
    #     self.interface()

    #     print("...")
    #     sleep_and_clear(3)
    #     self.interface()

    #     print("Goblin: ghrghnhthnhmrht")
    #     sleep_and_clear(5)
    #     self.interface()

    #     print("You wake up, beeing dragged by leg, by stinking, ugly, little creature.\n \
    # You use other leg to kick goblin in the back!\n \
    # Right after hit, he drops your leg and falls.\n \
    # In one quick swing of your sword you kill the beast.")
    #     sleep_and_clear(16)

        self.loot.goblin_loot()
        sleep_and_clear(1)
        self.interface()

    #     print("After the fight, you look around. You have no idea where you are or how far you are from the entrance.\n \
    # You find yourself among the ruins of a structure that appears to have been built by an extinct civilization.\n \
    # The sky is completely black, with no stars in sight, and everything is illuminated by something resembling a violet sun.\n \
    # Here and there, clusters of gray-green grass grow.")
    #     sleep_and_clear(16)
    #     self.interface()

    #     print("Suddenly, from behind one of the 'buildings,' or what's left of it, you hear a noise approaching.\n \
    # You hide behind a pillar, and peeking out of the corner of your eye,\n \
    # you see a group of goblins with torches moving through the ruins,\n \
    # led by one much larger goblin clad in armor — clearly their leader.")
    #     sleep_and_clear(16)
    #     self.interface()

    #     print("You wait in hiding until the enemies pass you by.\n \
    # As soon as they move a safe distance away, you step out from behind the pillar.\n \
    # Looking around, you realize you are surrounded by goblins. You must tread very carefully.")
    #     sleep_and_clear(14)
    #     self.interface()

    #     print("Silently, you sneak through the deserted streets, occasionally avoiding encounters with more goblins,\n \
    # until you reach an old bridge guarded on both sides by towers.\n \
    # As you approach, you notice that the bridge is protected by stone doors,\n \
    # and at their center is a seal glowing red with some kind of inscription on it.")
    #     sleep_and_clear(14)
    #     self.interface()

    #     print("You approach the door and are just about to touch the seal when suddenly, you hear a voice.")
    #     sleep_and_clear(8)
    #     self.interface()

    #     print("Dundalion: Wait! don't do this!")
    #     sleep_and_clear(3)
    #     self.interface()

    #     print("Startled, you jump back and instinctively draw your sword. You look around, but see no one.")
    #     sleep_and_clear(8)
    #     self.interface()

    #     print(f"{self.name}: Who's there? Show yourself!")
    #     sleep_and_clear(3)
    #     self.interface()

    #     print("Dundalion: Calm down, I won't harm you. My name is Dundalion.\n \
    # Like you, I am trapped here, though I have been for many centuries.")
    #     sleep_and_clear(8)
    #     self.interface()

    #     print("A translucent, bright white figure of an elf emerged from the wall.")
    #     sleep_and_clear(5)
    #     self.interface()

    #     print("Dundalion: This is no ordinary seal... It's protected by a password. \n \
    # You'll only pass if you can guess it. There are many similar doors throughout this labyrinth.")
    #     sleep_and_clear(8)
    #     self.interface()

    #     print("You approach the seal and read the riddle:")
    #     sleep_and_clear(4)
    #     self.interface()

        self.question.task_loop()
        if self.question.lost == True:
            print("Nie zgadłeś. Magiczna moc zadaje Ci ból a zagadka na pieczęci zmienia się...")
            # sleep_and_clear(4)
            self.question.lifes = ["\U0001F534", "\U0001F534", "\U0001F7E0", "\U0001F7E0", "\U0001F7E0", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2", "\U0001F7E2"]
            self.question.password = ["_"] * self.question.lenght  # Reset hasła
            self.question.used_letters = []  # Reset użytych liter
            self.question.lost = False  # Reset statusu przegranej
            self.question.task_loop()
        else:
            pass
        
        sleep_and_clear(1)
        self.interface()

        print("")
        sleep_and_clear(10)
        self.interface()

        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        # print("")
        # sleep_and_clear(10)
        # self.interface()
        

run = InitializeGame()
run.run_the_game()

















