from lab_python_oop.geometric_shape import geometricShape
from lab_python_oop.geometric_shape import figureColor
import math
from colorama import init, Fore, Back, Style


class circle(geometricShape):
    def __init__(self, name, radius, color):
        self.name = name
        self.radius = radius
        self.circleColor = figureColor(color)

    def square(self):
        return math.pi * self.radius ** 2

    init()

    def reper(self):
        print(
            f"{Fore.GREEN}Фигура: {self.name} | радиус: {self.radius} | площадь: {self.square()} | цвет: {self.circleColor.color}{Fore.RESET}")