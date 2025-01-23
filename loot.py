from player import PlayerData
import random
from enum import Enum
from system_functions import sleep_and_clear
class BodyLoot(PlayerData):
    def __init__(self):
        super().__init__()

    def event_method(self):
        self.event = Enum("event", ["empty", "crystal", "potion"])
        self.event_dict = {self.event.empty: 0.2, self.event.crystal: 0.4, self.event.potion: 0.4}
        self.event_list = list(self.event_dict.keys())
        self.event_propability = list(self.event_dict.values())

        self.drawn_event = random.choices(self.event_list, self.event_propability)[0]

    def colors_method(self, green, blue, purple, gold):
        self.colors = Enum("colors", ["green", "blue", "purple", "gold"])
        self.colors_dict = {self.colors.green: green, self.colors.blue: blue, self.colors.purple: purple, self.colors.gold: gold}
        self.colors_list = list(self.colors_dict.keys())
        self.colors_propability = list(self.colors_dict.values())

        self.drawn_color = random.choices(self.colors_list, self.colors_propability)[0]

    def loot_method(self):
        while True:
            search = input("Do you want to search the goblin? Ansewar 'y' or 'n'\n")
            search.lower()

            if search == "y" or search == "Y": 
                if self.drawn_event == self.event.crystal:
                    if self.drawn_color == self.colors.green:
                        self.damage += 5
                        self.interface()
                        print("You find green crystal, your damage is increased by 5 points")
                        break

                    elif self.drawn_color == self.colors.blue:
                        self.damage += 10
                        self.interface()
                        print("You find blue crystal, your damage is increased by 10 points")
                        break

                    elif self.drawn_color == self.colors.purple:
                        self.damage += 20
                        self.interface()
                        print("You find purple crystal, your damage is increased by 20 points")
                        break

                    elif self.drawn_color == self.colors.gold:
                        self.damage += 50
                        self.interface()
                        print("You find gold crystal, your damage is increased by 50 points")
                        break

                elif self.drawn_event == self.event.potion:
                    if self.drawn_color == self.colors.green:
                        self.damage += 5
                        self.interface()
                        print("You find green potion, your damage is increased by 5 points")
                        break

                    elif self.drawn_color == self.colors.blue:
                        self.damage += 10
                        self.interface()
                        print("You find blue potion, your damage is increased by 10 points")
                        break

                    elif self.drawn_color == self.colors.purple:
                        self.damage += 20
                        self.interface()
                        print("You find purple potion, your damage is increased by 20 points")
                        break

                    elif self.drawn_color == self.colors.gold:
                        self.damage += 50
                        self.interface()
                        print("You find gold potion, your damage is increased by 50 points")
                        break

                elif self.drawn_event == self.event.empty:
                    print("empty")
                    break
            elif search == "n" or search == "N":
                break
            else:
                print("You put the wrong letter, try again")
                sleep_and_clear(3)
                continue

    def goblin_loot(self):
        self.event_method()
        self.colors_method(0.6, 0.2, 0.15, 0.05)
        self.loot_method()

