from abc import ABC

from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal, ABC):

    def make_sound(self):
        return "Squeak"

    def gained_weight(self):
        return 0.10

    def eat_food(self):
        return [Vegetable, Fruit]


class Dog(Mammal, ABC):

    def make_sound(self):
        return "Woof!"

    def gained_weight(self):
        return 0.40

    def eat_food(self):
        return [Meat]


class Cat(Mammal, ABC):

    def make_sound(self):
        return "Meow"

    def gained_weight(self):
        return 0.30

    def eat_food(self):
        return [Meat, Vegetable]


class Tiger(Mammal, ABC):

    def make_sound(self):
        return "ROAR!!!"

    def gained_weight(self):
        return 1.00

    def eat_food(self):
        return [Meat]
