# we need to create a class for the human player that is a child of the player class
from player.player import Player
# import gestures

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name: ") # will ask the user for a name for the human player
        self.score = 0
# we need to create a method that will allow the human player to choose a gesture
    def choose_gesture(self):
        pass
# we need to create a method that will allow the human player to display their score
    def display_score(self):
        pass