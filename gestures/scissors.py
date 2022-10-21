# as a developer, I want to create a class for the scissors gesture
# class Scissors:
#     def __init__(self):
#         self.name = "scissors"
#         self.beats = ["paper", "lizard"]
#         self.beaten_by = ["rock", "spock"]
# scissors class that inherits from the gesture class
from gestures.gesture import Gesture
class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "scissors"
        self.beats = ["paper", "lizard"]
        self.beaten_by = ["rock", "spock"]