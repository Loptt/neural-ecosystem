from organism import Organism


class Ecosystem:

    def __init__(self, number_organisms):
        self.organisms = []
        for i in range(number_organisms):
            self.organisms.append(Organism(0, 0, 1))

    def step(self):
        pass
