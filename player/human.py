# we need to create a class for the human player that is a child of the player class
from time import sleep
from player.player import Player
from gestures.creategesturelist import create_gestures
class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("\nPlease enter your name: ") # will ask the user for a name for the human player
        self.score = 0
        self.choice = ""
        self.gesture_list = create_gestures()
# we need to create a method that will allow the human player to choose a gesture
    def choose_gesture(self):
        print('\nPlease choose a gesture: ')
        sleep(1)
        print('\n1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print('4. Lizard')
        print('5. Spock')
        sleep(1)
        try:
            choice = int(input('\n\t\tPlease enter the number next to the gesture you would like to choose: '))
            if choice == 1:
                self.choice = self.gesture_list[0]
            elif choice == 2:
                self.choice = self.gesture_list[1]
            elif choice == 3:
                self.choice = self.gesture_list[2]
            elif choice == 4:
                self.choice = self.gesture_list[3]
            elif choice == 5:
                self.choice = self.gesture_list[4]
            else:
                print('\nPlease enter a valid number.')
                return self.choose_gesture() # recursion
        except ValueError as error:
            print(f'{error} is not a valid choice. Please try again.')
            return self.choose_gesture()