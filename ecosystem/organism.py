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

    def step(self, size):
        # TODO: Change these to decay in function of other things (size, speed, etc.)
        self.hunger -= 0.01 * size
        self.thirst -= 0.01 * size

        self.x += random.uniform(-2, 2) * size
        self.y += random.uniform(-2, 2) * size

    def eats_food(self, dist):
        if dist < self.size:
            self.hunger = self.hunger + 50 if self.hunger + 50 < 100 else 100.0
            return True

        return False

    def calculate_perception(self, x, y):
        dx = self.x - x
        dy = self.y - y
        dist = math.sqrt(dx**2 + dy**2)
        angle = math.atan(dy / dx)

        return {"dist": dist, "angle": angle}
