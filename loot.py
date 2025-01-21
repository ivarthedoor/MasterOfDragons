from player import PlayerData
import random
from enum import Enum
class BodyLoot(PlayerData):
    def goblin_loot(self):
        event = Enum("event", ["empty", "crystal", "potion"])
        event_dict = {event.empty: 0.2, event.crystal: 0.4, event.potion: 0.4}
        event_list = list(event_dict.keys())
        event_propability = list(event_dict.values())

        drawn_event = random.choices(event_list, event_propability)[0]



        colors = Enum("colors", ["green", "blue", "purple", "gold"])
        colors_dict = {colors.green: 0.6, colors.blue: 0.2, colors.purple: 0.15, colors.gold: 0.05}
        colors_list = list(colors_dict.keys())
        colors_propability = list(colors_dict.values())

        drawn_color = random.choices(colors_list, colors_propability)[0]

        if drawn_event == event.crystal:
            if drawn_color == colors.green:
                self.damage += 5
                self.interface()
                print("You find green crystal, your damage is increased by 5 points")

            elif drawn_color == colors.blue:
                self.damage += 10
                self.interface()
                print("You find blue crystal, your damage is increased by 10 points")

            elif drawn_color == colors.purple:
                self.damage += 20
                self.interface()
                print("You find purple crystal, your damage is increased by 20 points")

            elif drawn_color == colors.gold:
                self.damage += 50
                self.interface()
                print("You find gold crystal, your damage is increased by 50 points")

        elif drawn_event == event.potion:
            if drawn_color == colors.green:
                self.damage += 5
                self.interface()
                print("You find green potion, your damage is increased by 5 points")

            elif drawn_color == colors.blue:
                self.damage += 10
                self.interface()
                print("You find blue potion, your damage is increased by 10 points")

            elif drawn_color == colors.purple:
                self.damage += 20
                self.interface()
                print("You find purple potion, your damage is increased by 20 points")

            elif drawn_color == colors.gold:
                self.damage += 50
                self.interface()
                print("You find gold potion, your damage is increased by 50 points")

        elif drawn_event == event.empty:
            print("empty")




