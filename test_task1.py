import unittest
from task1 import solve


class TestTask(unittest.TestCase):
    def test_small(self):
        self.assertEqual(solve(10, 2, 3), 9)

    def test_big(self):
        self.assertEqual(solve(2, 1000000000, 999999999), 1999999998)

    def test_square(self):
        self.assertEqual(solve(4, 1, 1), 2)


if __name__ == "__main__":
    unittest.main()
