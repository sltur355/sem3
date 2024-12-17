import math
from abc import ABC, abstractmethod


class geometricShape(ABC):
    @abstractmethod
    def square(self): pass


class figureColor:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value
