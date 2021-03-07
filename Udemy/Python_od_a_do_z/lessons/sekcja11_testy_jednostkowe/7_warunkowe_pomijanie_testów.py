
"""
Opis metod:

    unittest.skip(reason)
        pomija oznaczony test

    unittest.skipIf(condition, reason)
        pomija zaznaczony test jeżeli warunek jest prawdziwy

    unittest.skipUnless(condition, reason)
        pomija zaznaczony test, chyba, że warunek jest prawdziwy

    unittest.expectedFailure()
        oznacza test jako oczekiwany błąd, jeżeli test będzie niepowodzeniem
        nie zostanie policzony jako błąd
"""

import unittest


class SimpleTest(unittest.TestCase):

    x = 6
    y = 2

    @unittest.skip('Pomiń')
    def test_add(self):
        result = self.x + self.y
        self.assertEqual(result, 8)

    @unittest.skipIf(x < y, 'Pomiń1')
    def test_sub(self):
        result = self.x - self.y
        self.assertEqual(result, 4)

    @unittest.skipUnless(y == 0, 'Pomiń2')
    def test_div(self):
        result = self.x / self.y
        self.assertEqual(result, 3)

    @unittest.expectedFailure
    def test_mul(self):
        result = self.x * self.y
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
