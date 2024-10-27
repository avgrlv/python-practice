from fourth.zoo.food import Food


class Animal:
    def __init__(self, name):
        self.food = Food(100)
        self.name = name

    def eat(self, food: Food):
        self.food.nutrition += food.nutrition
        print(f"Животное {self.name} насытилось, текущая питательность: {self.food.nutrition}")

    def is_hungry(self):
        return self.food.nutrition <= 15.0
