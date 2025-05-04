import math
from abc import ABC, abstractmethod
from .exceptions import InvalidShapeError


class Shape(ABC):
    """Абстрактный класс для фигур"""

    @abstractmethod
    def calculate_area(self) -> float:
        """Вычисляем площадь фигур"""
        pass


class Circle(Shape):
    """Круг, заданный по радиусу"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidShapeError("Радиус должен быть больше нуля")
        self.radius = radius
        print(f"Круг с радиусом {self.radius}")

    def calculate_area(self) -> float:
        """
        Вычисляет площадь круга 3,14*r2
        :return: area - площадь круга
        """
        area = (self.radius ** 2) * math.pi
        print(f"Площадь круга = {area}")
        return area


class Triangle(Shape):
    """Треугольник, заданный 3мя сторонами"""

    def __init__(self, side1: float, side2: float, side3: float):
        if not (side1 > 0 and side2 > 0 and side3 > 0):
            raise InvalidShapeError("Все стороны должны быть больше нуля")
        side = sorted([side1, side2, side3])
        a, b, c = side
        if a + b <= c:
            raise InvalidShapeError("Невозможно построить треугольник стороны а + б больше c")
        self.side_a = a
        self.side_b = b
        self.side_c = c
        print(f"Треугольник со сторонами {self.side_a}, {self.side_b} и {self.side_c}")

    def calculate_area(self) -> float:
        """
        Вычисляет площадь треугольника.
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        :return: area - Площадь треугольника
        """
        s = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        print(f"Площадь треугольника {self.side_a}, {self.side_b} и {self.side_c}, равна {area}")
        return area

    def is_right_angle(self) -> bool:
        """
        Проверяем, является ли треугольник прямоугольным.
        :return: True|False
        """
        is_right_angle = math.isclose(self.side_a ** 2 + self.side_b ** 2, self.side_c ** 2)
        print(f"Треугольник прямоугольный: {is_right_angle}")
        return is_right_angle


def calculate_area(shape: Shape) -> float:
    """Площадь любой фигуры"""
    if not isinstance(shape, Shape):
         raise TypeError("Объект должен быть экземпляром класса, унаследованного от Shape.")
    return shape.calculate_area()

Triangle(3,4,5).is_right_angle()