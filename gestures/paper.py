# as a developer, I want to create a class for the paper gesture
# class Paper:
#     def __init__(self):
#         self.name = "paper"
#         self.beats = ["rock", "spock"]
#         self.beaten_by = ["scissors", "lizard"]
# creating a paper class that inherits from the gesture class
from gestures.gesture import Gesture
class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "paper"
        self.beats = ["rock", "spock"]
        self.beaten_by = ["scissors", "lizard"]