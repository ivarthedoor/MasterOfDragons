import random
from enum import Enum
from utils import sleep_and_clear


class Chests:
    def __init__(self):
        self.add_health_points_chest = 0
        self.add_damage_points_chest = 0

    def event_method(self):
        self.event = Enum("event", [
            "empty",
            "chest"
        ])
        self.event_dict = {self.event.empty: 0.1, self.event.chest: 0.9}
        self.event_list = list(self.event_dict.keys())
        self.event_probability = list(self.event_dict.values())
        self.drawn_event = random.choices(self.event_list, self.event_probability)[0]

    def colors_method(self, green, blue, purple, gold):
        self.colors = Enum("colors", [
            "green",
            "blue",
            "purple",
            "gold"
        ])
        self.colors_dict = {
            self.colors.green: green,
            self.colors.blue: blue,
            self.colors.purple: purple,
            self.colors.gold: gold
        }
        self.colors_list = list(self.colors_dict.keys())
        self.colors_probability = list(self.colors_dict.values())
        self.drawn_color = random.choices(self.colors_list, self.colors_probability)[0]

    def print_color(self):
        return self.drawn_color.name  # Automatyczne pobranie nazwy koloru

    def item_method(self):
        self.item = Enum("item", [
            "helmet",
            "bracers",
            "gauntlets",
            "chestplate",
            "trousers",
            "boots",
            "chainmail",
            "shield",
            "ring_of_regeneration",
            "cape",

            "sword",
            "axe",
            "mace",
            "frying_pan",
            "stick",
            "bow",
            "staff",
            "dagger",
            "double_axe",
            "amulet_of_fire"
        ])
        self.item_list = list(self.item)
        self.item_probability = [1 / len(self.item_list)] * len(self.item_list)
        self.drawn_item = random.choices(self.item_list, self.item_probability)[0]

    def calculate_points(self):
        # Przyznanie punktów na podstawie koloru i typu przedmiotu
        color_multiplier = {
            "green": 1,
            "blue": 2,
            "purple": 3,
            "gold": 5
        }
        base_health_points = 5
        base_damage_points = 5

        # Obliczenia punktów dla ubrania
        if self.drawn_item.name in [
            "helmet", "bracers", "gauntlets", "chestplate",
            "trousers", "boots", "chainmail", "shield",
            "ring_of_regeneration", "cape"
        ]:
            self.add_health_points_chest = base_health_points * color_multiplier[self.print_color()]
            self.add_damage_points_chest = 0  # Ubrania nie zwiększają obrażeń

        # Obliczenia punktów dla broni
        elif self.drawn_item.name in [
            "sword", "axe", "mace", "frying_pan", "stick",
            "bow", "staff", "dagger", "double_axe", "amulet_of_fire"
        ]:
            self.add_damage_points_chest = base_damage_points * color_multiplier[self.print_color()]
            self.add_health_points_chest = 0  # Broń nie zwiększa zdrowia

    def search_chest(self):
        # Losowanie zdarzenia, koloru i przedmiotu za każdym razem
        self.event_method()
        self.colors_method(0.5, 0.3, 0.15, 0.05)  # Szanse na kolory
        self.item_method()

        if self.drawn_event == self.event.chest:
            self.calculate_points()  # Obliczenie punktów na podstawie losowania

            # Wyświetlenie wyników
            if self.add_health_points_chest > 0:
                print(f"You find a {self.print_color()} {self.drawn_item.name}, health is increased by {self.add_health_points_chest} points!")
            elif self.add_damage_points_chest > 0:
                print(f"You find a {self.print_color()} {self.drawn_item.name}, damage is increased by {self.add_damage_points_chest} points!")

            sleep_and_clear(5)

        elif self.drawn_event == self.event.empty:
            # Skrzynia jest pusta
            print("The chest is empty.")
            sleep_and_clear(5)

    def run_search_chest(self):
        while True:
            player_input = input("Do you want to search the chest? (y/n)\n").strip().lower()
            if player_input == "y":
                self.search_chest()
            elif player_input == "n":
                print("You chose not to search the chest. Exiting.")
                break
            else:
                print("Invalid input. Please type 'y' or 'n'.")

run = Chests()
run.run_search_chest()




















# import random

# green = []
# purple = []
# golden = []
# color = ["Green", "Purple", "Golden"]
# random_color = random.choice(color)

# clothes = {
#     "Helmet": random_color,
#     "Bracelets": random_color,
#     "Gauntlets": random_color,
#     "Armor": random_color,
#     "Trousers": random_color
# }

# weapons = {
#     "Sword": color,
#     "Axe": color,
#     "Mace": color,
#     "Pan": color,
#     "Stick": color,
#     "Bow": color,
#     "Crossbow": color
# }


# print(clothes)