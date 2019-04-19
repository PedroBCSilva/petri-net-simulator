class Place:
    name = ''
    arcs = []
    marks = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def produce_mark(self):
        self.marks += 1

    def consume_mark(self):
        self.marks -= 1

    def add_arc(self, arc):
        self.arcs.append(arc)
