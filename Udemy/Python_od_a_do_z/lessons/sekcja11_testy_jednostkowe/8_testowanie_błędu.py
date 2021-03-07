
"""
assertRaises(expection, callable, *args, **kwargs)
    Testuje czy błąd zostanie wyrzucony. Test jest zdany, gdy oczekiwany błąd
    zostanie podniesiony, w przeciwnym razie test jest nie zdany.
"""

import unittest


def div(a, b):
    return a / b


class RaiseTest(unittest.TestCase):

    def test_raise(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)


if __name__ == '__main__':
    unittest.main()
