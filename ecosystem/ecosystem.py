import json
import random
from organism import Organism


class Ecosystem:

    def __init__(self, number_organisms):
        self.organisms = []
        for i in range(number_organisms):
            self.organisms.append(Organism(random.randint(0, 300), random.randint(0, 300), 15))

    def step(self):
        pass

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)