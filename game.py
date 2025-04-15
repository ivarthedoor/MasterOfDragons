from player import PlayerData
from players_choices import PlayersChoices
from questions_task import QuestionsTask
from npc import NpcCharacters
from enemies import Enemy
from chests import Chests
from loot import BodyLoot
from utils import sleep_and_clear, read_data
import random


class InitializeGame(PlayerData):
    def __init__(self):
        self.health = 100
        self.damage = 10
        self.choices = PlayersChoices()
        self.loot = BodyLoot()
        self.chest = Chests()
        self.question = QuestionsTask()
        self.npc = NpcCharacters()
        self.ancalacans_dialogue = self.npc.ancalacan()
        self.narration = self.npc.narrator()
        self.dundalions_dialogue = self.npc.dundalion()
        self.enemy = Enemy()
        self.goblin = self.enemy.goblin()
        self.first_boss = self.enemy.first_boss()
        super().__init__()

    def interface(self):
        self.health += self.loot.add_health_points_loot
        self.health += self.question.punish_points
        self.health += self.chest.add_health_points_chest
        self.damage += self.loot.add_damage_points_loot
        self.damage += self.chest.add_damage_points_chest
        self.loot.add_health_points_loot = 0
        self.loot.add_damage_points_loot = 0
        self.chest.add_health_points_chest = 0
        self.chest.add_damage_points_chest = 0
        self.question.punish_points = 0
        print(f"{self.name}\n❤️: {self.health}\n🗡️: {self.damage}\n")

    def print_interface(self, a, b):
        print(a)
        sleep_and_clear(b)
        self.interface()

    def event_and_interface(self, a, b):
        a
        sleep_and_clear(b)
        self.interface()

    def reset_questions_data(self):
        self.interface()
        print("You failed to guess. A magical force inflicts pain upon you, and the riddle on the seal changes...")
        sleep_and_clear(4)
        self.question.question_variable = random.choice(read_data())
        if "answer" not in self.question.question_variable or "description" not in self.question.question_variable:
            raise ValueError("Invalid question format in data.")
        self.question.lenght = len(self.question.question_variable["answer"])
        self.question.lifes = ["🛡️"] * 10
        self.question.password = ["_"] * self.question.lenght
        self.question.used_letters = []
        self.question.lost = False
        self.question.task_loop()

    def door_seal_question(self):
        self.question.task_loop()
        while self.question.lost:
            self.reset_questions_data()

    def fight(self, enemy):
        while True:
            if self.health <= 0:
                self.health = 0
                print(f"{self.name}\n❤️: {self.health}\n{enemy['name']}\n❤️: {enemy['hp']}\n{enemy['name']} won, you died...")
                break
            elif enemy['hp'] <= 0:
                enemy['hp'] = 0
                print(f"{self.name}\n❤️: {self.health}\n{enemy['name']}\n❤️: {enemy['hp']}\nYou won, {enemy['name']} died...")
                break
            else:
                player_dmg = random.randint(0, self.damage)
                enemy_dmg = random.randint(0, enemy['dmg'])
                if enemy_dmg == 0:
                    print(f"{enemy['name']} missed you")
                    sleep_and_clear(1)
                    continue
                elif player_dmg == 0:
                    print(f"You missed {enemy['name']}")
                    sleep_and_clear(1)
                    continue
                else:
                    print(f"{self.name}\n❤️: {self.health}\n{enemy['name']}\n❤️: {enemy['hp']}")
                    self.health -= enemy_dmg
                    print(f"{enemy['name']} hits You with: {enemy_dmg}")
                    sleep_and_clear(1)

                    print(f"{self.name}\n❤️: {self.health}\n{enemy['name']}\n❤️: {enemy['hp']}")
                    enemy['hp'] -= player_dmg
                    print(f"You hit {enemy['name']} with: {player_dmg}")
                    sleep_and_clear(1)

    def run_the_game(self):
        print(self.ancalacans_dialogue[1])
        sleep_and_clear(3)
        self.initialize_player()
        sleep_and_clear(3)
        self.choices.first_choice()
        self.interface()

        self.print_interface(self.narration[1], 16)

        self.print_interface("...", 3)

        self.print_interface("Goblin: ghrghnhthnhmrht", 5)

        self.print_interface(self.narration[2], 16)

        self.fight(self.first_boss)

        self.event_and_interface(self.loot.goblin_loot(), 1)

        self.print_interface(self.narration[3], 16)

        self.print_interface(self.narration[4], 16)

        self.print_interface(self.narration[5], 14)

        self.print_interface(self.narration[6], 14)

        self.print_interface(self.narration[7], 8)

        self.print_interface(self.dundalions_dialogue[1], 3)

        self.print_interface(self.narration[8], 8)

        self.print_interface(f"{self.name}: Who's there? Show yourself!", 3)

        self.print_interface(self.dundalions_dialogue[2], 8)

        self.print_interface(self.narration[9], 5)

        self.print_interface(self.dundalions_dialogue[3], 8)

        self.print_interface(self.narration[10], 4)

        self.event_and_interface(self.door_seal_question(), 1)

        self.print_interface("grrzzzt...", 3)

        self.print_interface(self.narration[11], 8)

        self.print_interface("test text text text text text text text text text", 4)

        self.chest.run_search_chest()
        sleep_and_clear(1)
        self.interface()


run = InitializeGame()
run.run_the_game()
