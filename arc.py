class Arc:
    name = ''
    place = None
    transition = None

    def __init__(self, name, place, transition):
        self.name = name
        self.place = place
        self.transition = transition

    def check_mark_available(self):
        return self.place.marks if self.place.marks > 0 else None
    
    def add_transition(self, transition):
        self.transition = transition
    
