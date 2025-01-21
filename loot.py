from player import PlayerData
import random
from enum import Enum
class BodyLoot(PlayerData):
    def goblin_loot(self):
        event = Enum("event", ["empty", "loot"])
        event_dict = {event.empty: 0.2, event.loot: 0.8}
        event_list = list(event_dict.keys())
        event_propability = list(event_dict.values())

        drawn_event = random.choices(event_list, event_propability)[0]



        colors = Enum("colors", ["green", "blue", "purple", "gold"])
        colors_dict = {colors.green: 0.6, colors.blue: 0.2, colors.purple: 0.15, colors.gold: 0.05}
        colors_list = list(colors_dict.keys())
        colors_propability = list(colors_dict.values())

        drawn_color = random.choices(colors_list, colors_propability)[0]

        if drawn_event == event.loot:
            if drawn_color == colors.green:
                print(f"You get green {self.damage}")
                self.damage += 5
                print(self.damage)
            elif drawn_color == colors.blue:
                print(f"You get blue {self.damage}")
                self.damage += 10
                print(self.damage)
            elif drawn_color == colors.purple:
                print(f"You get purple {self.damage}")
                self.damage += 20
                print(self.damage)
            elif drawn_color == colors.gold:
                print(f"You get gold! {self.damage}")
                self.damage += 50
                print(self.damage)
        elif drawn_event == event.empty:
            print("empty")




