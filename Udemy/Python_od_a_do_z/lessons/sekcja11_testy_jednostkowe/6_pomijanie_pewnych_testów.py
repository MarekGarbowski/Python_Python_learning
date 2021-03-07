
# Przekazać do skryptu aby pominą pewne testy

import unittest


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class SimpleTest(unittest.TestCase):

    def test_add(self):
        self.skipTest('Pomiń')
        self.assertEqual(add(4, 5), 9)

    # @unittest.skip('Pomiń 1')  #  Używanie dekoratorów do pomijania testów
    def test_sub(self):
        self.assertEqual(sub(10, 8), 2)


if __name__ == "__main__":
    unittest.main()
