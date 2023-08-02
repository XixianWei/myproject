# TASK 2
import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self):
        """Method documentation"""
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Triangle perimeter:", perim)
        return perim

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = 2 * (self.a + self.b)
        print("Rectangle perimeter:", perim)
        return perim

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def calc_perimeter(self):
        perim = 4 * self.a
        print("Square perimeter:", perim)
        return perim

# Create instances of each class
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(5, 8)
square = Square(4)

# Print the result of calc_perimeter method for each instance
triangle.calc_perimeter()
rectangle.calc_perimeter()
square.calc_perimeter()
