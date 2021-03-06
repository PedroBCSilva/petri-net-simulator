from place import Place
from arc import Arc
from transition import Transition
from output import Output
from cycle import Cycle
from optparse import OptionParser

class PetriNet:
    file_name = ''
    places = []
    transitions = []
    arcs = []
    cycles = []
    start = []

    def __init__(self, file_name):
        self.file_name = file_name
        self.init_data()
        self.process()
        output = Output(self.cycles, self.places, self.transitions)
        output.print()


    def init_data(self):
        with open (file_name, 'rt') as file:
            for line in file:
                if "new_place" in line:
                    (text, name, marks, is_start_text) = line.split()
                    is_start = False
                    if is_start_text == 'True':
                        is_start = True
                    else:
                        is_start = False
                    place = Place(name, int(marks), is_start)
                    self.places.append(place)
                    if place.entry:
                        self.start.append(place)                  
                elif "new_transition" in line:
                    (text, name) = line.split()
                    self.transitions.append(Transition(name))
                elif "new_arc" in line:
                    (text, name_arc, name_place, name_transition, arc_type, cost) = line.split()
                    place = self.find_place_by_name(name_place)
                    transition = self.find_transition_by_name(name_transition)
                    arc = Arc(name_arc, place, transition, int(cost))
                    if arc_type == 'arc_in':
                        place.add_arc(arc)
                        transition.add_arc_in(arc)
                    else:
                        transition.add_arc_out(arc)

                    self.arcs.append(arc)

    def find_place_by_name(self, name):
        for i in range(len(self.places)):
            if self.places[i].name == name:
                return self.places[i]

    def find_transition_by_name(self, name):
        for i in range(len(self.transitions)):
            if self.transitions[i].name == name:
                return self.transitions[i]

    def get_next(self):
        for transition in self.transitions:
            if transition.is_enabled() == True:
                return transition

    def transition_enabled(self):
        for transition in self.transitions:
            if transition.is_enabled() == True:
                return True
        return False

    def subtract_marks(self, tplace, cost):
        for i in range(len(self.places)):
            if tplace == self.places[i]:
                self.places[i].consume_mark(cost)
                return

    def add_marks(self, tplace, cost):
        for i in range(len(self.places)):
            if tplace == self.places[i]:
                self.places[i].produce_mark(cost)
                return

    def toggle_transition(self, transition):
        for i in range(len(self.transitions)):
            if transition == self.transitions[i]:
                self.transitions[i].toggle()
                return

    def evaluate(self):
        for transition in self.transitions:
            enable = True
            for arc in transition.arcs_in:
                if arc.place.marks < arc.cost:
                    enable = False
                    break
            if enable == True:
                for i in range(len(self.transitions)):
                    if transition == self.transitions[i]:
                        self.transitions[i].toggle()
                        break

    def start_empty(self):
        empty = True
        for start in self.start:
            if start.marks != 0:
                empty = False
        return empty

    def process(self):
        self.evaluate()
        self.cycles.append(Cycle(self.places, self.transitions))
        while(self.start_empty() == False or self.transition_enabled() == True):
            
            while(self.transition_enabled() == True):
                transition = self.get_next()
                for arc in transition.arcs_in:
                    tplace = arc.place
                    self.subtract_marks(tplace, arc.cost)
                for arc in transition.arcs_out:
                    tplace = arc.place
                    self.add_marks(tplace, arc.cost)
                self.toggle_transition(transition)
            self.evaluate()
            self.cycles.append(Cycle(self.places, self.transitions))

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--file", dest="filename", help="Path of file", default="input1.txt", type="string")

    (options, args) = parser.parse_args()

    file_name = options.filename

    petri_net = PetriNet(file_name)
