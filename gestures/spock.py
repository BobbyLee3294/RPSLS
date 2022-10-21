# as a devloper, I want to create a class for the spock gesture
# class Spock:
#     def __init__(self):
#         self.name = "spock"
#         self.beats = ["scissors", "rock"]
#         self.beaten_by = ["paper", "lizard"]
# spock class that inherits from the gesture class
from gestures.gesture import Gesture
class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "spock"
        self.beats = ["scissors", "rock"]
        self.beaten_by = ["paper", "lizard"]