# we need to create a class for the computer player that is a child of the player class
from player.player import Player
from gestures.creategesturelist import create_gestures
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = random.choice(["J.A.R.V.I.S.", "HAL 9000", "Wintermule", "Max Headroom", "GLaDOS"]) # unlike the human player, the computer player will have a list of names that it will randomly choose from
        self.score = 0
        self.gesture = ""
# also unlike the human player, the computer player will have a method that will allow it to randomly choose a gesture
    def choose_gesture(self):
        gesture_choice = random.randint(1, 5)
        if gesture_choice == 1:
            self.gesture = create_gestures()[0]
        elif gesture_choice == 2:
            self.gesture = create_gestures()[1]
        elif gesture_choice == 3:
            self.gesture = create_gestures()[2]
        elif gesture_choice == 4:
            self.gesture = create_gestures()[3]
        elif gesture_choice == 5:
            self.gesture = create_gestures()[4]