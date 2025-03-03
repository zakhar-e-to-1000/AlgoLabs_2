import unittest
from task1 import solve, BinaryTree


class Task1Test(unittest.TestCase):
    def test_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(4)
        self.assertEqual(solve(root), True)

    def test_2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(2)
        root.left.left.left = BinaryTree(2)
        root.right = BinaryTree(4)
        self.assertEqual(solve(root), False)


if __name__ == '__main__':
    unittest.main()
