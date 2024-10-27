from fourth.zoo.animal import Animal
from fourth.zoo.food import Food
from fourth.zoo.grass import Grass


class Herbivorous(Animal, Grass):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food: Food):
        if isinstance(food, Grass):
            super().eat(food)
        else:
            print(f"{self.name} такое не ест")
