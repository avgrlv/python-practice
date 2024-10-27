import math


class Point:
    def __init__(self, name):
        self.name = name
        self.x = float(input(f"Введите x для точки {name}: "))
        self.y = float(input(f"Введите y для точки {name}: "))

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __gt__(self, other):
        return (math.fabs(self.x) > math.fabs(other.x)) and (math.fabs(self.y) > math.fabs(other.y))

    def __ge__(self, other):
        return (math.fabs(self.x) >= math.fabs(other.x)) and (math.fabs(self.y) >= math.fabs(other.y))
