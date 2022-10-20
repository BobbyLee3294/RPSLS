# we need to create a class for the computer player that is a child of the player class
from player.player import Player
# import the gestures for the player to choose from
from gestures.lizard import Lizard
from gestures.paper import Paper
from gestures.rock import Rock
from gestures.scissors import Scissors
from gestures.spock import Spock
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Johnny 5" # unlike the human player, the computer player will have a name of its own
        self.score = 0
        self.choice = ""
# also unlike the human player, the computer player will have a method that will allow it to randomly choose a gesture
    def choose_gesture(self):
        gesture_choice = random.randint(1, 5)
        if gesture_choice == 1:
            self.choice = Rock()
        elif gesture_choice == 2:
            self.choice = Paper()
        elif gesture_choice == 3:
            self.choice = Scissors()
        elif gesture_choice == 4:
            self.choice = Lizard()
        elif gesture_choice == 5:
            self.choice = Spock()