from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food, ABC):
    pass


class Fruit(Food, ABC):
    pass


class Meat(Food, ABC):
    pass


class Seed(Food, ABC):
    pass
