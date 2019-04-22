from place import Place
from transition import Transition
from copy import deepcopy

class Cycle:
    places = []
    transitions = []

    def __init__(self, places, transitions):
        self.places = deepcopy(places)
        self.transitions = deepcopy(transitions)
