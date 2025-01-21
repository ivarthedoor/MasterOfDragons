import random
from enum import Enum
class BodyLoot:
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
            print(drawn_color)
        elif drawn_event == event.empty:
            print("empty")




