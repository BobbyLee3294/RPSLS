# this file is used to create the player class
from gestures.creategesturelist import create_gestures
class Player:
# a player will have a name and a score
    def __init__(self):
        self.name = ""
        self.score = 0
        self.gesture = ""
        self.gestures = create_gestures()
# a player will have a method that will allow them to choose a gesture
    def choose_gesture(self):
        pass
