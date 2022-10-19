# we need to create a class for the computer player that is a child of the player class
from player.player import Player
import random
# import gestures

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer" # unlike the human player, the computer player will have a name of "Computer"
        self.score = 0
        self.choice = ""

# also unlike the human player, the computer player will have a method that will allow it to randomly choose a gesture
    def choose_gesture(self):
        self.choice = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])