import math
import unittest

from geometry import Circle, Triangle, InvalidShapeError, Shape,calculate_area


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        c1 = Circle(1)
        self.assertAlmostEqual(c1.calculate_area(), math.pi)
        c2 = Circle(5.5)
        self.assertAlmostEqual(c2.calculate_area(), math.pi * (5.5 ** 2))

    def test_circle_invalid_radius(self):
        with self.assertRaisesRegex(InvalidShapeError, 'Радиус должен быть больше нуля'):
            Circle(0)
        with self.assertRaisesRegex(InvalidShapeError, 'Радиус должен быть больше нуля'):
            Circle(-1)

    def test_triangle_area_heron(self):
        # Равносторонний
        t1 = Triangle(5, 5, 5)
        expected_area_t1 = (math.sqrt(3) / 4) * (5 ** 2)
        self.assertAlmostEqual(t1.calculate_area(), expected_area_t1)

        # Прямоугольный
        t2 = Triangle(3, 4, 5)
        self.assertAlmostEqual(t2.calculate_area(), 6.0)  # (3 * 4) / 2

        # Произвольный
        t3 = Triangle(7, 8, 9)
        s = (7 + 8 + 9) / 2  # 12
        expected_area_t3 = math.sqrt(s * (s - 7) * (s - 8) * (s - 9))  # sqrt(12*5*4*3) = sqrt(720)
        self.assertAlmostEqual(t3.calculate_area(), expected_area_t3)

    def test_triangle_invalid_sides(self):
        # Нулевая сторона
        with self.assertRaisesRegex(InvalidShapeError, "Все стороны должны быть больше нуля"):
            Triangle(3, 4, 0)
        # Отрицательная сторона
        with self.assertRaisesRegex(InvalidShapeError, "Все стороны должны быть больше нуля"):
            Triangle(3, -4, 5)
        # Неравенство треугольника
        with self.assertRaisesRegex(InvalidShapeError, "Невозможно построить треугольник стороны а + б больше c"):
            Triangle(1, 2, 3)  # 1 + 2 = 3
        with self.assertRaisesRegex(InvalidShapeError, "Невозможно построить треугольник стороны а + б больше c"):
            Triangle(10, 2, 3)  # 2 + 3 < 10

    def test_triangle_is_right_angled(self):
        t_right = Triangle(3, 4, 5)
        self.assertTrue(t_right.is_right_angle())

        t_right_shuffled = Triangle(5, 3, 4)
        self.assertTrue(t_right_shuffled.is_right_angle())

        t_not_right = Triangle(5, 5, 5) # Равносторонний
        self.assertFalse(t_not_right.is_right_angle())

        t_acute = Triangle(8, 9, 10) # Прямоугольный
        self.assertFalse(t_acute.is_right_angle())

        # С плавающей точкой
        t_float_right = Triangle(1, 1, math.sqrt(2))
        self.assertTrue(t_float_right.is_right_angle())

    def test_calculate_area_polymorphic(self):
        shapes: list[Shape] = [
            Circle(1),
            Triangle(3, 4, 5),
            Circle(2.5),
            Triangle(5, 5, 5)
        ]

        expected_areas = [
            math.pi,
            6.0,
            math.pi * (2.5 ** 2),
            (math.sqrt(3) / 4) * (5 ** 2)
        ]

        for i, shape in enumerate(shapes):
            # Проверяем, что функция работает для разных типов фигур
            self.assertAlmostEqual(calculate_area(shape), expected_areas[i])
            # Также проверяем прямой вызов метода объекта
            self.assertAlmostEqual(shape.calculate_area(), expected_areas[i])

    def test_calculate_area_polymorphic_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_area("not_a_shape")  # Передаем строку вместо Shape
        with self.assertRaises(TypeError):
            calculate_area(123)  # Передаем число вместо Shape

    if __name__ == '__main__':
        unittest.main()