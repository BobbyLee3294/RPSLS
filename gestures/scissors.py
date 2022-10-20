# as a developer, I want to create a class for the scissors gesture
class Scissors:
    def __init__(self):
        self.name = "scissors"
        self.beats = ["paper", "lizard"]
        self.beaten_by = ["rock", "spock"]
# as a developer, I want to create a method for the scissors gesture that will compare itself to the other gestures
def compare_gestures(self, gesture):
    if gesture.name in self.beats == ["paper", "lizard"]:
        return "win"
    elif gesture.name in self.beaten_by == ["rock", "spock"]:
        return "lose"
    else:
        return "tie"