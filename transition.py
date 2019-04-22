class Transition:
    name = ''
    arcs_in = []
    arcs_out = []
    enabled = False

    def __init__(self, name):
        self.name = name

    def add_arc_in(self, arc):
        self.arcs_in.append(arc)

    def add_arc_out(self, arc):
        self.arcs_out.append(arc)

    def toggle(self):
        self.enabled = not self.enabled

    def is_enabled(self):
        return self.enabled
