# as a developer, I want to create a class for the rock gesture
# class Rock:
#     def __init__(self):
#         self.name = "rock"
#         self.beats = ["scissors", "lizard"]
#         self.beaten_by = ["paper", "spock"]
# now the rock class will inherit from the gesture class
# remember that the gesture class is the parent class so it will have to be imported
from gestures.gesture import Gesture
class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = "rock"
        self.beats = ["scissors", "lizard"]
        self.beaten_by = ["paper", "spock"]