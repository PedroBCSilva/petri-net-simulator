class Place:
    name = ''
    arcs = []
    marks = 0
    entry = False

    def __init__(self, name, marks, entry):
        self.name = name
        self.marks = marks
        self.entry = entry

    def produce_mark(self):
        self.marks += 1

    def consume_mark(self):
        self.marks -= 1

    def add_arc(self, arc):
        self.arcs.append(arc)
