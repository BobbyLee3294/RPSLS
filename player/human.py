# we need to create a class for the human player that is a child of the player class
from player.player import Player
# import the gestures for the player to choose from
from gestures.lizard import Lizard
from gestures.paper import Paper
from gestures.rock import Rock
from gestures.scissors import Scissors
from gestures.spock import Spock
class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("\nPlease enter your name: ") # will ask the user for a name for the human player
        self.score = 0
        self.choice = ""
# we need to create a method that will allow the human player to choose a gesture
    def choose_gesture(self):
        gesture_choice = int(input("\nPlease choose a gesture:\n1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock\n"))
        if gesture_choice == 1:
            self.choice = Rock()
        elif gesture_choice == 2:
            self.choice = Paper()
        elif gesture_choice == 3:
            self.choice = Scissors()
        elif gesture_choice == 4:
            self.choice = Lizard()
        elif gesture_choice == 5:
            self.choice = Spock()
        else:
            print("\nInvalid choice. Please try again.")
            self.choose_gesture()