import unittest
from task1 import solve


class TestTask(unittest.TestCase):
    def test_normal(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(solve(arr), (3, 9))

    def test_sorted(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        arr.sort()
        self.assertEqual(solve(arr), (-1, -1))

    def test_one_element(self):
        arr = [1]
        self.assertEqual(solve(arr), (-1, -1))


if __name__ == '__main__':
    unittest.main()
