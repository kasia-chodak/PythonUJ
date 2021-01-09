import unittest


def sign(a):
    if a == 0:
        return 0
    # nie może być zero, sprawdzamy wcześniej
    return a // abs(a)


class Frac:
    """Klasa reprezentująca ułamki."""

    def gcd(self):  # największy wspólny dzielnik
        x = abs(self.x)
        y = abs(self.y)
        while y > 0:
            x, y = y, x % y
        return x

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError("You can't divide by 0.")
        self.x = sign(y) * x
        self.y = abs(y)

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return f"{self.x}"
        return f"{self.x}/{self.y}"

    def __repr__(self):   # zwraca "Frac(x, y)"
        if self.y == 1:
            return f"Frac({self.x})"
        return f"Frac({self.x}, {self.y})"

    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        gcd_self = self.gcd()
        gcd_other = other.gcd()
        return self.x // gcd_self == other.x // gcd_other and self.y // gcd_self == other.y // gcd_other

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return self.x * other.y > other.x * self.y

    def __ge__(self, other):
        return self == other or self > other

    def __add__(self, other):  # frac1+frac2, frac+int
        if isinstance(other, int):
            return Frac(self.x + self.y * other, self.y)
        return Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if isinstance(other, int):
            return Frac(self.x - self.y * other, self.y)
        return Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if isinstance(other, int):
            return Frac(self.x * other, self.y)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    #def __div__(self, other): pass  -- frac1/frac2, frac/int, Python 2

    #def __rdiv__(self, other): pass -- int/frac, Python 2

    def __truediv__(self, other):  # frac1/frac2, frac/int, Python 3
        if isinstance(other, int):
            return Frac(self.x, self.y * other)
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):  # int/frac, Python 3
        if isinstance(other, int):
            return Frac(self.y * other, self.x)
        return Frac(self.x * other.x, self.y * other.y)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

# Kod testujący moduł.


class TestFrac(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertNotEqual(str(Frac(1, 2)), "2")
        self.assertRaises(ValueError, Frac, *(3, 0))
        self.assertNotEqual(str(Frac(3, 1)), "3/1")
        self.assertEqual(str(Frac(3, 1)), "3")

    def test_repr(self):
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
        self.assertNotEqual(repr(Frac(1, 2)), "Frac(2)")
        self.assertRaises(ValueError, Frac, *(3, 0))
        self.assertNotEqual(repr(Frac(3, 1)), "Frac 3, 1")
        self.assertEqual(repr(Frac(3, 1)), "Frac(3)")

    def test_eq(self):
        self.assertEqual(Frac(5, 5), Frac(5, 5))
        self.assertNotEqual(Frac(5, 6), Frac(3, 3))
        self.assertEqual(Frac(3, 4), Frac(6, 8))
        self.assertNotEqual(Frac(3, 4), Frac(4, 3))

    def test_ne(self):
        self.assertEqual(Frac(5, 5), Frac(5, 5))
        self.assertNotEqual(Frac(5, 6), Frac(3, 3))
        self.assertEqual(Frac(3, 4), Frac(6, 8))
        self.assertNotEqual(Frac(3, 4), Frac(4, 3))

    def test_lt(self):
        self.assertLess(Frac(1, 2), Frac(3, 4))
        self.assertLess(Frac(1, 3), Frac(1, 2))
        self.assertLess(Frac(3, 2), Frac(2, 1))
        self.assertLess(Frac(2, 5), Frac(2, 3))
        self.assertLess(Frac(2, 5), Frac(5, 2))

    def test_le(self):
        self.assertLessEqual(Frac(1, 2), Frac(1, 2))
        self.assertLessEqual(Frac(1, 2), Frac(4, 8))
        self.assertLessEqual(Frac(3, 2), Frac(2, 1))
        self.assertLessEqual(Frac(2, 5), Frac(2, 3))
        self.assertLessEqual(Frac(1, 2), Frac(3, 4))

    def test_gt(self):
        self.assertGreater(Frac(3, 4), Frac(1, 2))
        self.assertGreater(Frac(1, 2), Frac(1, 3))
        self.assertGreater(Frac(2, 1), Frac(3, 2))
        self.assertGreater(Frac(2, 3), Frac(2, 5))
        self.assertGreater(Frac(5, 2), Frac(2, 5))

    def test_ge(self):
        self.assertGreaterEqual(Frac(3, 4), Frac(1, 2))
        self.assertGreaterEqual(Frac(1, 2), Frac(1, 3))
        self.assertGreaterEqual(Frac(3, 3), Frac(4, 4))
        self.assertGreaterEqual(Frac(2, 3), Frac(4, 6))
        self.assertGreaterEqual(Frac(5, 2), Frac(2, 5))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 4), Frac(3, 4))
        self.assertNotEqual(Frac(1, 2) + Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(1, 5) + 5, Frac(26, 5))
        self.assertEqual(4 + Frac(5, 3), Frac(17, 3))
        self.assertNotEqual(Frac(3, 5) + Frac(5, 3), Frac(15, 15))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 4), Frac(1, 4))
        self.assertNotEqual(Frac(1, 2) - Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(3, 5) - 4, Frac(-17, 5))
        self.assertNotEqual(2 - Frac(1, 4), Frac(8, 4))
        self.assertEqual(Frac(5, 3) - Frac(3, 5), Frac(16, 15))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 4), Frac(1, 8))
        self.assertNotEqual(Frac(1, 2) * Frac(1, 2), Frac(1, 3))
        self.assertEqual(Frac(3, 5) * 4, Frac(12, 5))
        self.assertNotEqual(Frac(1, 3) * Frac(5, 4), Frac(5, 7))
        self.assertEqual(5 * Frac(3, 4), Frac(15, 4))

    def test_truediv(self):
        self.assertEqual(Frac(1, 2) / 2, Frac(1, 4))
        self.assertNotEqual(Frac(1, 2) / Frac(1, 2), Frac(1, 4))
        self.assertEqual(Frac(3, 5) / Frac(5, 3), Frac(9, 25))
        self.assertNotEqual(Frac(1, 3) / 3, Frac(1, 1))
        self.assertEqual(12 / Frac(3, 4), Frac(16, 1))

    def test_pos(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))
        self.assertNotEqual(+Frac(1, 2), Frac(1, -2))
        self.assertEqual(+Frac(-3, 5), Frac(-3, 5))
        self.assertNotEqual(+Frac(1, 3), Frac(3, 1))
        self.assertEqual(+Frac(5, 4), Frac(5, 4))

    def test_neg(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertNotEqual(-Frac(1, 2), Frac(-1, -2))
        self.assertEqual(-Frac(-3, 5), Frac(3, 5))
        self.assertNotEqual(-Frac(1, 3), Frac(-3, 1))
        self.assertEqual(-Frac(5, 4), Frac(5, -4))

    def test_invert(self):
        self.assertEqual(~Frac(1, 2), Frac(2, 1))
        self.assertNotEqual(~Frac(1, 2), Frac(-1, 2))
        self.assertEqual(~Frac(-3, 5), Frac(5, -3))
        self.assertNotEqual(~Frac(1, 3), Frac(1, 1))
        self.assertEqual(~Frac(5, 4), Frac(4, 5))

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), (0.5))
        self.assertNotEqual(float(Frac(1, 2)), (-1 / 2))
        self.assertEqual(float(Frac(-3, 5)), (-3 / 5))
        self.assertNotEqual(float(Frac(1, 3)), (1 / 1))
        self.assertEqual(float(Frac(5, 4)), (5 / 4))

    def test_hash(self):
        self.assertEqual(hash(float(Frac(1, 2))), hash(Frac(1, 2)))
        self.assertNotEqual(hash(float(Frac(1, 2))), hash(Frac(-1 / 2)))
        self.assertEqual(hash(float(Frac(-3, 5))), hash(Frac(-3 / 5)))
        self.assertNotEqual(hash(float(Frac(1, 3))), hash(Frac(1 / 1)))
        self.assertEqual(hash(float(Frac(5, 4))), hash(Frac(5 / 4)))


if __name__ == '__main__':
    unittest.main()
