# we need to create a class for the human player that is a child of the player class
from time import sleep
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
        print('\nPlease choose a gesture: ')
        sleep(1)
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print('4. Lizard')
        print('5. Spock')
        sleep(1)
        gesture_choice = int(input(f"\nSelect your gesture {self.name}: "))
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