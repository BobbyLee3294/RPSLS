# as a developer, I want to create a class for the paper gesture
class Paper:
    def __init__(self):
        self.name = "paper"
        self.beats = ["rock", "spock"]
        self.beaten_by = ["scissors", "lizard"]
# as a developer, I want to create a method for the paper gesture that will compare itself to the other gestures
def compare_gestures(self, gesture):
    if gesture.name in self.beats ==["rock", "spock"]:
        return "win"
    elif gesture.name in self.beaten_by == ["scissors", "lizard"]:
        return "lose"
    else:
        return "tie"