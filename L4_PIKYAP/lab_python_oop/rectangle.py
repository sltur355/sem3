from lab_python_oop.geometric_shape import geometricShape
from lab_python_oop.geometric_shape import figureColor
from colorama import init, Fore, Back, Style


class Rectangle(geometricShape):
    def __init__(self, name, height, width, color):
        self.name = name
        self.width = width
        self.height = height
        self.rectangleColor = figureColor(color)

    def square(self):
        return self.width * self.height

    init()
    def reper(self):
        print(
            f"{Fore.GREEN}Фигура: {self.name} | длина: {self.height} | ширина: {self.width} | площадь: {self.square()} | цвет: {self.rectangleColor.color}{Fore.RESET}")
