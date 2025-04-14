class NpcCharacters:
    def ancalacan(self):
        # Ancalacan, fear of the east. Games main antagonist. Great dragon guarding the temple
        dialogues_level1 = {
            1: "    Ancalacan: Welcome Wanderer...\n \
        You shall fear, for I am a ghost of Ancalacan, fear of the east...\n \
        The greatest of all dragons...\n \
        You dare to attempt to my temple!\n \
        Who are you?! And What is your name?!",
            2: "ABC",
            3: "ABC",
            4: "ABC",
            5: "ABC",
            6: "ABC",
            7: "DEF"
        }
        return dialogues_level1
    
    def narrator(self):
        # description of actual events
        dialogues_level1 = {
            1: "You enter through ancient stone door, to an old, ruined hall.\n \
    walls and roof are full of holes, aeverything is covered in moss. You feel the smell of water and rot.\n \
    You make few steps inside and right after you enter the room, something hits you from the back!",
            2: "You wake up, beeing dragged by leg, by stinking, ugly, little creature.\n \
    You use other leg to kick goblin in the back!\n \
    Right after hit, he drops your leg and falls.\n \
    In one quick swing of your sword you kill the beast.",
            3: "After the fight, you look around. You have no idea where you are or how far you are from the entrance.\n \
    You find yourself among the ruins of a structure that appears to have been built by an extinct civilization.\n \
    The sky is completely black, with no stars in sight, and everything is illuminated by something resembling a violet sun.\n \
    Here and there, clusters of gray-green grass grow.",
            4: "Suddenly, from behind one of the 'buildings,' or what's left of it, you hear a noise approaching.\n \
    You hide behind a pillar, and peeking out of the corner of your eye,\n \
    you see a group of goblins with torches moving through the ruins,\n \
    led by one much larger goblin clad in armor — clearly their leader.",
            5: "You wait in hiding until the enemies pass you by.\n \
    As soon as they move a safe distance away, you step out from behind the pillar.\n \
    Looking around, you realize you are surrounded by goblins. You must tread very carefully.",
            6: "Silently, you sneak through the deserted streets, occasionally avoiding encounters with more goblins,\n \
    until you reach an old bridge guarded on both sides by towers.\n \
    As you approach, you notice that the bridge is protected by stone doors,\n \
    and at their center is a seal glowing red with some kind of inscription on it.",
            7: "You approach the door and are just about to touch the seal when suddenly, you hear a voice.",
            8: "Startled, you jump back and instinctively draw your sword. You look around, but see no one.",
            9: "A translucent, bright white figure of an elf emerged from the wall.",
            10: "You approach the seal and read the riddle:",
            11: "The stone doors open with a heavy scraping sound. You step onto the bridge, and Dundalion follows behind you.",
        }
        return dialogues_level1

    def dundalion(self):
        # soul of a fallen hero. Player meets him after first task. Dundalion helps player through all game
        dialogues_level1 = {
            1: "Dundalion: Wait! don't do this!",
            2: "Dundalion: Calm down, I won't harm you. My name is Dundalion.\n \
        Like you, I am trapped here, though I have been for many centuries.",
            3: "Dundalion: This is no ordinary seal... It's protected by a password. \n \
    You'll only pass if you can guess it. There are many similar doors throughout this labyrinth.",
            4: "ABC",
        }
        return dialogues_level1
