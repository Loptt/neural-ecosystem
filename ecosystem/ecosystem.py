import json
import random
from organism import Organism
from food import Food


class Ecosystem:

    def __init__(self, number_organisms, food_amount):
        self.organisms = []
        self.foods = []

        for i in range(number_organisms):
            self.organisms.append(Organism(random.randint(
                0, 1000), random.randint(0, 1000), 15))

        for i in range(food_amount):
            self.foods.append(
                Food(random.randint(0, 1000), random.randint(0, 1000)))

    def run(self):
        while True:
            self.step()

    def step(self):
        for org in self.organisms:
            org.step()

            for food in self.foods:
                if not food.valid:
                    continue
                if org.eats_food(food.x, food.y):
                    food.valid = False

            if org.hunger <= 0 or org.thirst <= 0:
                org.alive = False

        self.foods = [f for f in self.foods if f.valid]
        self.organisms = [o for o in self.organisms if o.alive]

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
