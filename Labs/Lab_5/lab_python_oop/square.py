from lab_python_oop import abstract, colour, rectangle


class kvadrat(rectangle.rectangle):
    def __init__(self, length=10, colour_="Белый"):
        rectangle.rectangle.__init__(self, length=length, colour_=colour_)
        self.__name = "Квадрат"

    def square(self):
        res = self._length**2
        return res

    def get_name(self):
        return self.__name

    def get_colour(self):
        return self._colour

    def repr(self):
        print(
            f"Название фигуры: {self.get_name()}\n"
            f"Цвет фигуры: {self.get_colour()}\n"
            f"Площадь фигуры: {self.square()}\n" + "\n"
        )
