
"""
assertListEqual - sprawdza czy dwie listy są równe
assertTupleEqual - sprawdza czy dwie tuple są równe
assertSetEqual - sprawdza czy dwa zbiory są równe
assertDictEqual - sprawdza czy dwa słowniki są równe
"""

import unittest

class SimplTest(unittest.TestCase):

    def test_1(self):
        self.assertListEqual([1, 2, 23, 4], [1, 2, 3, 4])

    def test_2(self):
        self.assertTupleEqual((1, 22), (1, 2))

    def test_3(self):
        self.assertSetEqual({1, 2}, {12, 2})

    def test_4(self):
        self.assertDictEqual({'12': 'jeden', '2': 'dwa'}, {'1': 'jeden', '2': 'dwa'})


if __name__ == '__main__':
    unittest.main()
