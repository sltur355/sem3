from lab_python_oop.geometric_shape import figureColor
from lab_python_oop.rectangle import Rectangle
from colorama import init, Fore, Back, Style

class quadrate(Rectangle):
    def __init__(self, name, side, color):
        self.name = name
        self.side = side
        self.quadrateColor = figureColor(color)

    def square(self):
        return self.side**2

    init()
    def reper(self):
        print(f"{Fore.GREEN}Фигура: {self.name} | длина стороны: {self.side} | площадь: {self.square()} | цвет: {self.quadrateColor.color}{Fore.RESET}")
