# this is the main class for the gesture recognition
# it is the parent class for all the other gestures that will be created
class Gesture:
    def __init__(self):
        # this is the name of the gesture
        self.name = ""
        # this is the list of gestures that this gesture beats
        self.beats = []
        # this is the list of gestures that beat this gesture
        self.beaten_by = []