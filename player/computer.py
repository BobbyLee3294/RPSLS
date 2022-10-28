# we need to create a class for the computer player that is a child of the player class
from player.player import Player
from gestures.creategesturelist import create_gestures
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = random.choice(["J.A.R.V.I.S.", "HAL 9000", "Wintermule", "Max Headroom", "GLaDOS"]) # unlike the human player, the computer player will have a list of names that it will randomly choose from
        self.score = 0
        self.choice = ""
        self.gesture_list = create_gestures()
# also unlike the human player, the computer player will have a method that will allow it to randomly choose a gesture
    def choose_gesture(self):
        self.choice = random.choice(self.gesture_list)