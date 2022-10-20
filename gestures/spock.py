# as a devloper, I want to create a class for the spock gesture
class Spock:
    def __init__(self):
        self.name = "spock"
        self.beats = ["scissors", "rock"]
        self.beaten_by = ["paper", "lizard"]
# as a developer, I want to create a method for the spock gesture that will compare itself to the other gestures
def compare_gestures(self, gesture):
    if gesture.name in self.beats == ["scissors", "rock"]:
        return "win"
    elif gesture.name in self.beaten_by == ["paper", "lizard"]:
        return "lose"
    else:
        return "tie"
        