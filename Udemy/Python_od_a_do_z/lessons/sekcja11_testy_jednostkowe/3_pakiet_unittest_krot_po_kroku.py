
"""
Tworzenie testu jednostkowego:
1. Zaimportowanie unitest
2. Zdefiniowanie funkcji do testowania
3. Stworzenie przypadku testowego używając klasy unitest.TestCase
4. Zdefiniowanie testu jako metody klasy TestCase
5. Call assert function
6. Assert function wywoła błąd assertionError jeżeli otzrymamy błąd
7. Wywołaj funkcję main() z modułu unittest
"""
import unittest


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7, msg='Powinno być 7')


if __name__ == '__main__':
    unittest.main()
