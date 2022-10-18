# we need to create a class for the computer player that is a child of the player class
from player.player import Player
# import gestures

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer" # unlike the human player, the computer player will have a name of "Computer"
        self.score = 0
# we need to create a method that will allow the computer player to choose a gesture
    def choose_gesture(self):
        pass
# we need to create a method that will allow the computer player to display their score
    def display_score(self):
        return self.score