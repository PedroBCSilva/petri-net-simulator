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

    def __init__(self, file_name):
        self.file_name = file_name
        self.init_data()
        self.print_data()
        self.process()
        output = Output(self.cycles, self.places, self.transitions)
        output.print()


    def init_data(self):
        with open (file_name, 'rt') as file:
            for line in file:
                if "new_place" in line:
                    (text, name, marks) = line.split()
                    self.places.append(Place(name, int(marks), False))
                    # TODO TIRAR O FALSE E COLOCAR SE É ENTRADA OU NÃO
                elif "new_transition" in line:
                    (text, name) = line.split()
                    self.transitions.append(Transition(name))
                elif "new_arc" in line:
                    (text, name_arc, name_place, name_transition, arc_type) = line.split()
                    place = self.find_place_by_name(name_place)
                    transition = self.find_transition_by_name(name_transition)
                    arc = Arc(name_arc, place, transition)

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

    def print_data(self):
        print("Places")
        for place in self.places:
            print(place.name, '-', place.marks)

        print('=================')

        print("Transitions")
        for transition in self.transitions:
            print(transition.name)

        print('=================')

        for arc in self.arcs:
            print("arc:", arc.name)
            print("place:", arc.place.name)
            print("transition:", arc.transition.name)

    def process(self):
        #while(not entrada empty && not transaction enabled)
        self.cycles.append(Cycle(self.places, self.transitions))


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--file", dest="filename", help="Path of file", default="input.txt",
                     type="string")

    (options, args) = parser.parse_args()

    file_name = options.filename

    petri_net = PetriNet(file_name)
