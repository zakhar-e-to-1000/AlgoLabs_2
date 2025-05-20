import unittest
from main import solve


class TestMain(unittest.TestCase):
    def test_300(self):
        self.assertAlmostEqual(solve(100, [1, 1, 1, 1]), 300.0, 2)

    def test_big(self):
        self.assertAlmostEqual(solve(4, [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28,
                               2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]), 2738.178533742236, 2)

    def test_basic(self):
        self.assertAlmostEqual(solve(4, [100, 2, 100, 2, 100]), 396.32, 2)


if __name__ == '__main__':
    unittest.main()
