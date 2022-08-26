import json
import random
from organism import Organism
from food import Food


class Ecosystem:

    def __init__(self, number_organisms, food_amount, step_size):
        self.organisms = []
        self.foods = []
        self.step_size = step_size

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
            org.step(self.step_size)
            perceptions = []

            for food in self.foods:
                if not food.valid:
                    continue

                perception = org.calculate_perception(food.x, food.y)
                perceptions.append(perception)

                if org.eats_food(perception["dist"]):
                    food.valid = False

            if org.hunger <= 0 or org.thirst <= 0:
                print("Organism dead...")
                org.alive = False

        self.foods = [f for f in self.foods if f.valid]
        self.organisms = [o for o in self.organisms if o.alive]
        
        print("Organisms: ", len(self.organisms))
        print("Food: ", len(self.foods))

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
