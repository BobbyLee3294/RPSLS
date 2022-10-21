# as a developer, I want to create a class for the lizard gesture
# class Lizard:
#     def __init__(self):
#         self.name = "lizard"
#         self.beats = ["paper", "spock"]
#         self.beaten_by = ["rock", "scissors"]
# lizard class that inherits from the gesture class
from gestures.gesture import Gesture
class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "lizard"
        self.beats = ["paper", "spock"]
        self.beaten_by = ["rock", "scissors"]