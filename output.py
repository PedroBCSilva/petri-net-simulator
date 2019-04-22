from prettytable import PrettyTable
from cycle import Cycle
from place import Place
from transition import Transition
from colorama import init, Fore, Style

class Output:
    cycles = []
    places = []
    transitions = []
    cycle_row = []

    def __init__(self, cycles, places, transitions):
        self.cycles = cycles
        self.places = places
        self.transitions = transitions
        init()

    def prepare_rows(self):
        i = 0
        for cycle in self.cycles:
            row = []
            i += 1
            row.append(str(i))
            for place in cycle.places:
                row.append(str(place.marks))
            for transition in cycle.transitions:
                if transition.is_enabled() == True:
                    row.append("\033[92m" + str(transition.enabled) + Style.RESET_ALL)
                else:
                    row.append("\033[91m" + str(transition.enabled) + Style.RESET_ALL)
            self.cycle_row.append(row)

    def print(self):
        table = PrettyTable(["\033[93m Ciclo" + Style.RESET_ALL])
        i = 0

        for column in self.places:
            name = name = "\033[93m" + column.name  + Style.RESET_ALL
            table.add_column(name, "")

        i = 0
        for column in self.transitions:
            i += 1
            name = "\033[93m T" + str(i)  + Style.RESET_ALL
            table.add_column(name, "")

        self.prepare_rows()

        for row in self.cycle_row:
            table.add_row(row)

        print(table)
