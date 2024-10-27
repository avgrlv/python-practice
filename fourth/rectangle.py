import math

from fourth.point import Point


class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def get_height(self):
        return math.fabs(self.p1.y - self.p2.y)

    def get_width(self):
        return math.fabs(self.p1.x - self.p2.x)

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimetr(self):
        return (self.get_width() + self.get_height()) * 2

    def __str__(self):
        return (f"Прямоугольник задан точками: p1 = {self.p1}; p2 = {self.p2}\n"
                f"Высота    = {self.get_height()}\n"
                f"Ширина    = {self.get_width()}\n"
                f"Площадь   = {self.get_area()}\n"
                f"Периметр  = {self.get_perimetr()}")

    def __contains__(self, item: Point):
        return (self.p1.x <= item.x <= self.p2.x) and (self.p1.y <= item.y <= self.p2.y)
