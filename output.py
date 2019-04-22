from prettytable import PrettyTable
from cycle import Cycle
from place import Place
from transition import Transition

class Output:
    cycles = []
    places = []
    transitions = []
    cycle_row = []

    def __init__(self, cycles, places, transitions):
        self.cycles = cycles
        self.places = places
        self.transitions = transitions

    def prepare_rows(self):
        i = 0
        for cycle in self.cycles:
            row = []
            i += 1
            row.append(str(i))
            for place in cycle.places:
                row.append(str(place.marks))
            for transition in cycle.transitions:
                row.append(str(transition.enabled))
            self.cycle_row.append(row)

    def print(self):
        table = PrettyTable(['Ciclo'])
        i = 0

        for column in self.places:
            # i += 1
            # name = "L" + str(i)
            name = column.name
            table.add_column(name, "")

        i = 0
        for column in self.transitions:
            i += 1
            name = "T" + str(i)
            table.add_column(name, "")

        self.prepare_rows()

        for row in self.cycle_row:
            table.add_row(row)

        print(table)
