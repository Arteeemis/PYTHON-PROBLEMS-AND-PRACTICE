from lab_python_oop import abstract, colour


class rectangle(abstract.figure):
    def __init__(self, height=0, length=0, colour_="Белый"):
        self._length = length
        self.__height = height
        self._colour = colour.colour(colour_)
        self._name = "Прямоугольник"

    def square(self):
        res = self.__height * self._length
        return res

    def get_name(self):
        return self._name

    def get_colour(self):
        return self._colour

    def repr(self):
        print(
            f"Название фигуры: {self.get_name()}\n"
            f"Цвет фигуры: {self.get_colour()}\n"
            f"Площадь фигуры: {self.square()}\n" + "\n"
        )
