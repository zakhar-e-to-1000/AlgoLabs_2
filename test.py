import unittest

from main import solve


class TestMST(unittest.TestCase):

    def test_simple_triangle(self):
        edges = [(0, 1, 1), (1, 2, 2), (0, 2, 3)]
        self.assertEqual(solve(edges, 3), 3)

    def test_single_edge(self):
        edges = [(0, 1, 10)]
        self.assertEqual(solve(edges, 2), 10)

    def test_multiple_equal_msts(self):
        edges = [
            (0, 1, 1),
            (1, 2, 1),
            (0, 2, 1)
        ]
        self.assertEqual(solve(edges, 3), 2)

    def test_large_graph(self):
        edges = [
            (0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2),
            (2, 3, 4), (3, 4, 2), (4, 5, 6)
        ]
        self.assertEqual(solve(edges, 6), 14)


if __name__ == '__main__':
    unittest.main()
