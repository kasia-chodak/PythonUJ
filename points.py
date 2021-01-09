import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie"""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):  # obsługa point1 == point2
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        if not isinstance(other, Point):
            return self
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        if not isinstance(other, Point):
            return self
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        if not isinstance(other, Point):
            return self
        return self.x * other.x, self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D (liczba)
        if not isinstance(other, Point):
            return self
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# kod testujący moduł


class TestPoint(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Point(3, 7) + Point(5, 4), Point(8, 11))
        self.assertNotEqual(Point(3, 7) + Point(5, 4), Point(18, 30))
        self.assertEqual(Point(10, 6) + Point(13, 17), Point(23, 23))
        self.assertNotEqual(Point(10, 6) + Point(13, 17), Point(24, 22))

    def test_substract(self):
        self.assertEqual(Point(3, 7) - Point(5, 4), Point(-2, 3))
        self.assertNotEqual(Point(3, 7) - Point(5, 4), Point(2, 11))
        self.assertEqual(Point(10, 6) - Point(13, 17), Point(-3, -11))
        self.assertNotEqual(Point(10, 6) - Point(13, 17), Point(3, 17))

    def test_multiply(self):
        self.assertEqual(Point(3, 7) * Point(5, 4), (15, 28))
        self.assertNotEqual(Point(3, 7) * Point(5, 4), (8, 11))
        self.assertEqual(Point(10, 6) * Point(13, 17), (130, 102))
        self.assertNotEqual(Point(10, 6) * Point(13, 17), (23, 22))

    def test_cross(self):
        self.assertEqual(Point(3, 4).cross(Point(4, 6)), 2)
        self.assertNotEqual(Point(3, 4).cross(Point(4, 6)), 7)
        self.assertEqual(Point(8, 6).cross(Point(6, 10)), 44)
        self.assertNotEqual(Point(8, 6).cross(Point(6, 10)), 17)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertNotEqual(Point(3, 4).length(), 7)
        self.assertEqual(Point(8, 6).length(), 10)
        self.assertNotEqual(Point(8, 6).length(), 17)

    def test_hash(self):
        self.assertEqual(Point.__hash__(Point(5, 5)), hash((5, 5)))
        self.assertNotEqual(Point.__hash__(Point(5, 5)), hash((3, 3)))
        self.assertEqual(hash(Point(3, 4)), hash((3, 4)))
        self.assertNotEqual(hash(Point(3, 4)), hash((4, 3)))

    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertNotEqual(str(Point(1, 2)), "(3, 3)")
        self.assertEqual(str(Point(3, 5)), "(3, 5)")
        self.assertNotEqual(str(Point(3, 5)), "(5, 8)")

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")
        self.assertNotEqual(repr(Point(1, 2)), "Point(3, 3)")
        self.assertEqual(repr(Point(3, 5)), "Point(3, 5)")
        self.assertNotEqual(repr(Point(3, 5)), "Point(5, 8)")

    def test_eq_ne(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertNotEqual(Point(1, 2), Point(2, 1))
        self.assertNotEqual(Point(4, 5), 7)
        self.assertNotEqual(Point(4, 5), Point(4, 6))


if __name__ == '__main__':
    unittest.main()
