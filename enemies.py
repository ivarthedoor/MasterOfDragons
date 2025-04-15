class Enemy:
    def goblin(self):
        enemy_stats = {
            'name': "Goblin",
            'hp': 30,
            'dmg': 10
        }
        return enemy_stats

    def archer_goblin(self):
        enemy_stats = {
            'name': "Archer Goblin",
            'hp': 40,
            'dmg': 15
        }
        return enemy_stats

    def goblin_mage(self):
        enemy_stats = {
            'name': "Goblin Mage",
            'hp': 60,
            'dmg': 25
        }
        return enemy_stats

    def goblin_warlord(self):
        enemy_stats = {
            'name': "Goblin Warlord",
            'hp': 100,
            'dmg': 35
        }
        return enemy_stats

    def first_boss(self):
        enemy_stats = {
            'name': "Kharogath",  # secret shadow
            'tekst': "Kharogath: You dare step into the shadows where my dominion reigns?\n \
              I am Kharogath, the unseen blade, the whisper of death. Your light will falter before my eternal darkness.",
            'hp': 600,
            'dmg': 60
        }
        return enemy_stats

    def second_boss(self):
        enemy_stats = {
            'name': "Volrathor",  # the destroyer
            'tekst': "Volrathor: I am Volrathor, breaker of worlds! My power knows no bounds, and every swing of my hammer crushes hope itself.\n \
              Prepare to be obliterated!",
            'hp': 800,
            'dmg': 80
        }
        return enemy_stats

    def third_boss(self):
        enemy_stats = {
            'name': "Eryndalys",  # master of ilusion
            'tekst': "Eryndalys: Ah, a brave soul lost in the labyrinth of my making. I am Eryndalys, the weaver of dreams and nightmares.\n \
              What you see is not what you face... Can you even trust your own eyes?",
            'hp': 900,
            'dmg': 100
        }
        return enemy_stats

    def fourth_boss(self):
        enemy_stats = {
            'name': "Thalrog",  # dragon blood
            'tekst': "Thalrog: Foolish mortal! You face Thalrog, heir to the draconic bloodline!\n \
              My flames will scorch the very ground beneath you, and my strength will crush your feeble resolve.",
            'hp': 1000,
            'dmg': 110
        }
        return enemy_stats

    def fifth_boss(self):
        enemy_stats = {
            'name': "Narvathanna",  # iron breaker
            'tekst': "Narvathanna: Behold Narvathanna, the Iron Breaker! My armor is impenetrable, my will unyielding.\n \
              No force, mortal or divine, can shatter me. What hope do you cling to?",
            'hp': 1100,
            'dmg': 200
        }
        return enemy_stats

