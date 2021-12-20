import json
import random
from organism import Organism


class Ecosystem:

    def __init__(self, number_organisms):
        self.organisms = []
        for i in range(number_organisms):
            self.organisms.append(Organism(random.randint(0, 1000), random.randint(0,1000), 15))

    def run(self):
        while True:
            self.step()

    def step(self):
        for org in self.organisms:
            org.x += random.uniform(-0.1, 0.1)
            org.y += random.uniform(-0.1, 0.1)

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)