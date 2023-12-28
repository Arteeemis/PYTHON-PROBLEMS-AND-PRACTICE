from lab_python_oop import abstract, colour
from math import pi


class circle(abstract.figure):
    def __init__(self, rad=10, colour_="Белый "):
        self.__name = "Круг"
        self.__colour = colour.colour(colour_)
        self.__rad = rad

    def square(self):
        res = pi * self.__rad**2
        return res

    def get_name(self):
        return self.__name

    def get_colour(self):
        return self.__colour

    def repr(self):
        print(
            f"Название фигуры: {self.get_name()}\n"
            f"Цвет фигуры: {self.get_colour()}\n"
            f"Площадь фигуры: {self.square()}\n" + "\n"
        )
