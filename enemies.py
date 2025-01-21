import random

class Enemy:
    def __init__(self):
        self.name = None
        self.health = None
        self.attack = None
        self.tekst = None

    def goblin(self):
        self.name = "Goblin"
        self.health = 25
        self.attack = random.randint(1, 10)

    def archer_goblin(self):
        self.name = "Archer goblin"
        self.health = 30
        self.attack = random.randint(1, 15)

    def goblin_mage(self):
        self.name = "Goblin Mage"
        self.health = 40
        self.attack = random.randint(10, 30)

    def goblin_warlord(self):
        self.name = "Goblin Warlord"
        self.health = 55
        self.attack = random.randint(20, 60)

    def first_boss(self):
        self.name = "Kharogath" #secret shadow
        self.tekst = "Kharogath: You dare step into the shadows where my dominion reigns?\n \
              I am Kharogath, the unseen blade, the whisper of death. Your light will falter before my eternal darkness."
        self.health = 600
        self.attack = random.randint(20, 60)

    def second_boss(self):
        self.name = "Volrathor" #the destroyer
        self.tekst = "Volrathor: I am Volrathor, breaker of worlds! My power knows no bounds, and every swing of my hammer crushes hope itself.\n \
              Prepare to be obliterated!"
        self.health = 800
        self.attack = random.randint(30, 80)

    def third_boss(self):
        self.name = "Eryndalys" #master of ilusion
        self.tekst = "Eryndalys: Ah, a brave soul lost in the labyrinth of my making. I am Eryndalys, the weaver of dreams and nightmares.\n \
              What you see is not what you face... Can you even trust your own eyes?"
        self.health = 900
        self.attack = random.randint(40, 100)

    def fourth_boss(self):
        self.name = "Thalrog" #dragon blood
        self.tekst = "Thalrog: Foolish mortal! You face Thalrog, heir to the draconic bloodline!\n \
              My flames will scorch the very ground beneath you, and my strength will crush your feeble resolve."
        self.health = 1000
        self.attack = random.randint(50, 110)

    def fifth_boss(self):
        self.name = "Narvatharna" #iron breaker
        self.tekst = "Narvatharna: Behold Narvatharna, the Iron Breaker! My armor is impenetrable, my will unyielding.\n \
              No force, mortal or divine, can shatter me. What hope do you cling to?"
        self.health = 1100
        self.attack = random.randint(100, 200)