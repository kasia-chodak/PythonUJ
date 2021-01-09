from .points import Point
import math
import unittest

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        if (y1 == y2 == y3) or (x1 == x2 == x3) or ((x2 - x1)*(y3 - y1) == (y2 - y1)*(x3 - x1)):
            raise ValueError("Punkty są współliniowe")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return f"({self.pt1}, {self.pt2}, {self.pt3})"

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def side_sizes(self):
        return self.pt1.distance(self.pt2), self.pt1.distance(self.pt3), self.pt2.distance(self.pt3)

    def __eq__(self, other): # obsługa tr1 == tr2
        boki = self.side_sizes()
        boki_b = other.side_sizes()
        for bok in boki:
            if bok not in boki_b:
                return False
        return True

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):  # zwraca środek trójkąta
        return ((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    def area(self):  # pole powierzchni
        p = sum(self.side_sizes()) / 2
        return math.sqrt(p * (p - self.pt1.distance(self.pt2)) * (p - self.pt1.distance(self.pt3)) * (p - self.pt2.distance(self.pt3)))

    def move(self, x, y):  # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)

    def make4(self):   # zwraca krotkę czterech mniejszych
        pass
    # nie rozumiem, o co chodzi - czerech mniejszych trójkątów? jak utworzonych?

# Kod testujący moduł.

class TestTriangle(unittest.TestCase):

    def test_error(self):
        self.assertRaises(ValueError, Triangle, *(1, 2, 1, 3, 1, 4))

    def test_str(self):
        self.assertEqual(f"{str(Point(1, 2))}, {str(Point(2, 3))}, {str(Point(3, 1))}", "(1, 2), (2, 3), (3, 1)")
        self.assertNotEqual(f"{str(Point(1, 3))}, {str(Point(2, 10))}, {str(Point(7, 5))}", "(3, 1), (10, 2), (5, 7)")
        self.assertEqual(f"{str(Point(10, 20))}, {str(Point(12, 13))}, {str(Point(-3, -1))}", "(10, 20), (12, 13), (-3, -1)")
        self.assertNotEqual(f"{str(Point(1, 2))}, {str(Point(2, 3))}, {str(Point(3, 1))}", "(3, 1), (2, 3), (1, 2)")

    def test_repr(self):
        self.assertEqual(f"{repr(Triangle(1, 2, 2, 3, 3, 1))}", "Triangle(1, 2, 2, 3, 3, 1)")
        self.assertNotEqual(f"{repr(Triangle(1, 3, 10, 2, 5, 7))}", "Triangle(3, 1, 10, 2, 5, 7)")
        self.assertEqual(f"{repr(Triangle(10, 20, 12, 13, -3, -1))}", "Triangle(10, 20, 12, 13, -3, -1)")
        self.assertNotEqual(f"{repr(Triangle(1, 2, 2, 3, 3, 1))}", "Triangle(3, 1, 2, 3, 1, 2)")

    def test_eq_ne(self):
        self.assertEqual(Triangle(0, 1, 3, 1, 3, 5), Triangle(3, 5, 0, 1, 0, 5))
        self.assertNotEqual(Triangle(1, 3, 10, 2, 5, 7), Triangle(3, 1, 10, 2, 5, 7))
        self.assertNotEqual(Triangle(7, 8, 10, 10, 11, 12), Triangle(7, 9, 13, 13, 15, 17))
        self.assertEqual(Triangle(1, 2, 2, 3, 3, 1), Triangle(3, 1, 2, 3, 1, 2))

    def test_center(self):
        self.assertEqual(Triangle(0, 1, 3, 1, 3, 5).center(), (2, 7/3))
        self.assertNotEqual(Triangle(1, 3, 10, 2, 5, 7).center(), (4, 10))
        self.assertNotEqual(Triangle(7, 8, 10, 10, 11, 12).center(), (9, 1))
        self.assertEqual(Triangle(1, 2, 2, 3, 3, 1).center(), (2, 2))

    def test_area(self):
        self.assertEqual(Triangle(0, 1, 3, 1, 3, 5).area(), 6)
        self.assertNotEqual(Triangle(1, 3, 10, 2, 5, 7).area(), 12)
        self.assertNotEqual(Triangle(7, 8, 10, 10, 11, 12).area(), 81)
        self.assertEqual(Triangle(6, 0, 6, 8, 0, 0).area(), 24)

    def test_move(self):
        self.assertEqual(Triangle(0, 1, 3, 1, 3, 5).move(4, 5), Triangle(4, 6, 7, 6, 7, 10))
        self.assertNotEqual(Triangle(1, 3, 10, 2, 5, 7).move(5, 1), Triangle(1, 4, 50, 12, 5, 17))
        self.assertNotEqual(Triangle(7, 8, 10, 10, 11, 12).move(2, 3), Triangle(12, 14, 10, 12, 8, 9))
        self.assertEqual(Triangle(6, 0, 6, 8, 0, 0).move(1, 0), Triangle(7, 0, 7, 8, 1, 0))


if __name__ == '__main__':
    unittest.main()
