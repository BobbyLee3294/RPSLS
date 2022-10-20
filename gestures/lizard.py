# as a developer, I want to create a class for the lizard gesture
class Lizard:
    def __init__(self):
        self.name = "lizard"
        self.beats = ["paper", "spock"]
        self.beaten_by = ["rock", "scissors"]
# as a developer, I want to create a method for the lizard gesture that will compare itself to the other gestures
def compare_gestures(self, gesture):
    if gesture.name in self.beats == ["paper", "spock"]:
        return "win"
    elif gesture.name in self.beaten_by == ["rock", "scissors"]:
        return "lose"
    else:
        return "tie"