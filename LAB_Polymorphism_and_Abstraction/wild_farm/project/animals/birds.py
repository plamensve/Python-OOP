from abc import ABC

from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird, ABC):

    def make_sound(self):
        return "Hoot Hoot"

    def gained_weight(self):
        return 0.25

    def eat_food(self):
        return [Meat]


class Hen(Bird, ABC):

    def make_sound(self):
        return "Cluck"

    def gained_weight(self):
        return 0.35

    def eat_food(self):
        return [Meat, Vegetable, Fruit, Seed]
