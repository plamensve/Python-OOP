from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def gained_weight(self):
        ...

    @property
    @abstractmethod
    def eat_food(self):
        ...

    def feed(self, food: Food):
        if type(food) not in self.eat_food():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.gained_weight() * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        ...

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @staticmethod
    @abstractmethod
    def make_sound():
        ...

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
