import math
import random


class Organism:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.hunger = 100.0
        self.thirst = 100.0
        self.alive = True

    def step(self):
        # TODO: Change these to decay in function of other things (size, speed, etc.)
        self.hunger -= 0.0001
        self.thirst -= 0.0001

        self.x += random.uniform(-0.1, 0.1)
        self.y += random.uniform(-0.1, 0.1)

    def eats_food(self, x, y):
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        dist = math.sqrt(dx**2 + dy**2)

        if dist < self.size:
            self.hunger = self.hunger + 50 if self.hunger + 50 < 100 else 100.0
            return True

        return False
