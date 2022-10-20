# this method will take in the gesture classes and create a list of them
# this method will also return the list of gesture classes
# this method will be called in the game_logic file
from gestures.rock import Rock
from gestures.paper import Paper
from gestures.scissors import Scissors
from gestures.lizard import Lizard
from gestures.spock import Spock

def create_gestures():
    rock = Rock()
    paper = Paper()
    scissors = Scissors()
    lizard = Lizard()
    spock = Spock()
    gestures = [rock, paper, scissors, lizard, spock]
    return gestures