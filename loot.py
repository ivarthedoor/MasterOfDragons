from player import PlayerData
import random
from enum import Enum
from utils import sleep_and_clear
class BodyLoot():
    def __init__(self):
        self.add_damage_points = 0
        self.add_health_points = 0




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
            search = search.lower()  # Poprawka: zapewniamy, że input jest małymi literami

            if search == "y":  # Jeśli gracz chce szukać loot'u
                if self.drawn_event == self.event.crystal:
                    if self.drawn_color == self.colors.green:
                        self.add_damage_points = 5  # Zwiększamy damage o 5
                        print("You find green crystal, your damage is increased by 5 points")
                        return False

                    elif self.drawn_color == self.colors.blue:
                        self.add_damage_points = 10  # Zwiększamy damage o 10
                        print("You find blue crystal, your damage is increased by 10 points")
                        return False

                    elif self.drawn_color == self.colors.purple:
                        self.add_damage_points = 20 # Zwiększamy damage o 20
                        print("You find purple crystal, your damage is increased by 20 points")
                        return False

                    elif self.drawn_color == self.colors.gold:
                        self.add_damage_points = 50  # Zwiększamy damage o 50
                        print("You find gold crystal, your damage is increased by 50 points")
                        return False

                elif self.drawn_event == self.event.potion:
                    if self.drawn_color == self.colors.green:
                        self.add_health_points = 5  # Zwiększamy punkty życia o 5
                        print("You find green potion, your health is increased by 5 points")
                        return False

                    elif self.drawn_color == self.colors.blue:
                        self.add_health_points = 10  # Zwiększamy punkty życia o 10
                        print("You find blue potion, your health is increased by 10 points")
                        return False

                    elif self.drawn_color == self.colors.purple:
                        self.add_health_points = 20  # Zwiększamy punkty życia o 20
                        print("You find purple potion, your health is increased by 20 points")
                        return False

                    elif self.drawn_color == self.colors.gold:
                        self.add_health_points = 50  # Zwiększamy punkty życia o 50
                        print("You find gold potion, your health is increased by 50 points")
                        return False

                elif self.drawn_event == self.event.empty:
                    print("Body was empty.")  # Pusty loot
                    self.add_health_points = 0
                    self.add_damage_points = 0
                    return False

            elif search == "n":  # Gracz nie chce szukać loot'u
                self.add_health_points = 0
                self.add_damage_points = 0  
                return False
            else:  # Niewłaściwa odpowiedź
                self.add_health_points = 0
                self.add_damage_points = 0  
                print("Invalid input, try again.")
                sleep_and_clear(3)  # Poczekaj chwilę i wyczyść ekran

    def goblin_loot(self):
        self.event_method()
        self.colors_method(0.6, 0.2, 0.15, 0.05)
        self.loot_method()


