import unittest
from task2 import solve


class TestTask(unittest.TestCase):
    def test_normal(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(solve(arr), [(3, 9)])

    def test_sorted(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        arr.sort()
        self.assertEqual(solve(arr), [])

    def test_one_element(self):
        arr = [1]
        self.assertEqual(solve(arr), [])
    
    def test_teacher(self):
        arr = [1, 2, 3, 6, 5, 7, 8, 9, 11, 10, 12, 13, 14]
        self.assertEqual(solve(arr), [(3, 4), (8, 9)])
    
    def test_1(self):
        arr = [1, 4, 5, 2, 6, 7]
        self.assertEqual(solve(arr), [(1, 3)])

if __name__ == '__main__':
    unittest.main()
