from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    @abstractmethod
    def __repr__(self):
        ...

    @property
    @abstractmethod
    def make_sound(self):
        ...


class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"


class Kitten(Cat):
    def __init__(self, name: str, age: int, gender='Female'):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow'


class Tomcat(Cat):
    def __init__(self, name: str, age: int, gender='Male'):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Hiss'


kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)

