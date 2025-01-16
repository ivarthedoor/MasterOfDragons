import random

green = []
purple = []
golden = []
color = ["Green", "Purple", "Golden"]
random_color = random.choice(color)

clothes = {
    "Helmet": random_color,
    "Bracelets": random_color,
    "Gauntlets": random_color,
    "Armor": random_color,
    "Trousers": random_color
}

weapons = {
    "Sword": color,
    "Axe": color,
    "Mace": color,
    "Pan": color,
    "Stick": color,
    "Bow": color,
    "Crossbow": color
}


print(clothes)