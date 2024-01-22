#추상클래스
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_round(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.radius = r
    def get_area(self):
        return 3.14*self.radius**2


class Triangle(Shape):

    def __init__(self,s,h):
        self.side = s
        self.height = h

    def get_area(self):
        return self.side*self.height/2

    def get_round(self):
        return self.side*3

class Square(Shape):

    def __init__(self,s):
        self.side = s

    def get_area(self):
        return self.side**2

    def get_round(self):
        return self.side*4

a = Triangle(3,5)
b = Square(3)
print(a.get_area())
print(a.get_round())

