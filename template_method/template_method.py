"""Template method pattern module."""
from abc import ABC, abstractmethod
from cmath import pi


class Figure(ABC):
    """Figure abstract class."""
    def figure_info(self):
        """Get figure info."""
        print('{0}: perimeter={1}; area={2}; volume={3}.'.format(
            self.__get_class_name(), self.perimeter, self.area, self.volume
        ))

    def __get_class_name(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def perimeter(self):
        """Perimeter."""
        return 'No perimeter'

    @property
    @abstractmethod
    def area(self):
        """Area."""
        return 'No area'

    @property
    def volume(self):
        """Volume."""
        return 'No volume'


class Circle(Figure):
    """Circle class."""
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    @property
    def area(self):
        return pi * self.radius**2


class Square(Figure):
    """Square class."""
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    @property
    def perimeter(self):
        return 4 * self.side

    @property
    def area(self):
        return self.side**2


class Rectangle(Figure):
    """Rectangle class."""
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width


class Sphere(Figure):
    """Sphere class."""
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    @property
    def perimeter(self):
        return super().perimeter

    @property
    def area(self):
        return 4 * pi * self.radius**2

    @property
    def volume(self):
        return (4/3) * pi * self.radius**3


if __name__ == '__main__':
    CIRCLE = Circle(radius=4)
    CIRCLE.figure_info()

    SQUARE = Square(side=4)
    SQUARE.figure_info()

    RECTANGLE = Rectangle(length=4, width=8)
    RECTANGLE.figure_info()

    SPHERE = Sphere(radius=4)
    SPHERE.figure_info()
