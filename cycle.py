from place import Place
from transition import Transition

class Cycle:
    places = []
    transitions = []

    def __init__(self, places, transitions):
        self.places = places
        self.transitions = transitions
