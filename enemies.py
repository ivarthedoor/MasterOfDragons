import random

class Enemy:
    def __init__(self):
        self.enemy_name = None
        self.enemy_health = None
        self.enemy_attack = None
        self.enemy_tekst = None

    def goblin(self):
        enemy_stats = {
            'name': "Goblin",
            'hp': 30,
            'dmg': 10
        }
        return enemy_stats

    def archer_goblin(self):
        self.enemy_name = "Archer goblin"
        self.enemy_health = 20
        self.enemy_attack = random.randint(1, 15)

    def goblin_mage(self):
        self.enemy_name = "Goblin Mage"
        self.enemy_health = 40
        self.enemy_attack = random.randint(10, 30)

    def goblin_warlord(self):
        self.enemy_name = "Goblin Warlord"
        self.enemy_health = 55
        self.enemy_attack = random.randint(20, 60)

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
        self.enemy_name = "Volrathor"  # the destroyer
        self.enemy_tekst = "Volrathor: I am Volrathor, breaker of worlds! My power knows no bounds, and every swing of my hammer crushes hope itself.\n \
              Prepare to be obliterated!"
        self.enemy_health = 800
        self.enemy_attack = random.randint(30, 80)

    def third_boss(self):
        self.enemy_name = "Eryndalys"  # master of ilusion
        self.enemy_tekst = "Eryndalys: Ah, a brave soul lost in the labyrinth of my making. I am Eryndalys, the weaver of dreams and nightmares.\n \
              What you see is not what you face... Can you even trust your own eyes?"
        self.enemy_health = 900
        self.enemy_attack = random.randint(40, 100)

    def fourth_boss(self):
        self.enemy_name = "Thalrog"  # dragon blood
        self.enemy_tekst = "Thalrog: Foolish mortal! You face Thalrog, heir to the draconic bloodline!\n \
              My flames will scorch the very ground beneath you, and my strength will crush your feeble resolve."
        self.enemy_health = 1000
        self.enemy_attack = random.randint(50, 110)

    def fifth_boss(self):
        self.enemy_name = "Narvatharna"  # iron breaker
        self.enemy_tekst = "Narvatharna: Behold Narvatharna, the Iron Breaker! My armor is impenetrable, my will unyielding.\n \
              No force, mortal or divine, can shatter me. What hope do you cling to?"
        self.enemy_health = 1100
        self.enemy_attack = random.randint(100, 200)
