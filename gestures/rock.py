# as a developer, I want to create a class for the rock gesture
class Rock:
    def __init__(self):
        self.name = "rock"
        self.beats = ["scissors", "lizard"]
        self.beaten_by = ["paper", "spock"]
# as a developer, I want to create a method for the rock gesture that will compare itself to the other gestures
def compare_gestures(self, gesture):
    if gesture.name in self.beats == ["scissors", "lizard"]:
        return "win"
    elif gesture.name in self.beaten_by == ["paper", "spock"]:
        return "lose"
    else:
        return "tie"