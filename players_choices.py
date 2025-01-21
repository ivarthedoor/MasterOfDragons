from system_functions import sleep_and_clear

class PlayersChoices:
    def __init__(self):
        # self.first_dialog_choice = None
        self.first_d_choice = {1: "Wisdom", 2: "Power", 3: "Kill a dragon"}

    def get_choice(self, prompt, choices):
        while True:
            try:
                choice = int(input(prompt))
                if choice in choices:
                    return choice
                print(f"Input only: {', '.join(map(str, choices))}")
                sleep_and_clear(2)
            except ValueError:
                print("Invalid input. Please enter a number.")
                sleep_and_clear(2)

    def initialize_first_choice(self):
        self.first_dialog_choice = self.first_d_choice[self.get_choice("1. I seek for wisdom\n2. I seek for power\n3. I'm here to destroy you\n", self.first_d_choice.keys())]
        if self.first_dialog_choice == "Wisdom":
            sleep_and_clear(0.1)
            print("Ancalacan: You seek wisdom... A wise decision, young one.\nDifficult path lays ahead, first you must prove, you are worthy of my knowledge.")
            sleep_and_clear(10)
            print("Ancalacan: To prove that, you will have to overcome all challenges I will put on you.")
            sleep_and_clear(10)
        elif self.first_dialog_choice == "Power":
            sleep_and_clear(0.1)
            print("Ancalacan: You seek power... Many have fallen to that temptation.\nYet only few gained enough power to reach the end of the path.")
            sleep_and_clear(10)
            print("Ancalacan: We shall see if you are worthy of power of a dragon!")
            sleep_and_clear(10)
        elif self.first_dialog_choice == "Kill a dragon":
            sleep_and_clear(0.1)
            print("Ancalacan: You wish to destroy... There is a dark path ahead.\nAs dark as your soul might mecome if you will continue this path.\nThink wisely, hard task is before you... harder than you can imagine...")
            sleep_and_clear(10)
            print("Ancalacan: If you wish to kill me, you will have to reach me first Hahahahahaha!")
            sleep_and_clear(10)

