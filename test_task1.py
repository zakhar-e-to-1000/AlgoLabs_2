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

    def test_hollow(self):
        root = BinaryTree(2)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(2)
        self.assertEqual(solve(root), False)

class TestIsBalanced(unittest.TestCase):
    def test_empty_tree(self):
        self.assertTrue(solve(None))
    
    def test_single_node(self):
        self.assertTrue(solve(BinaryTree(1)))
    
    def test_balanced_tree(self):
        root = BinaryTree(1, BinaryTree(2), BinaryTree(3))
        self.assertTrue(solve(root))
    
    def test_unbalanced_tree(self):
        root = BinaryTree(1, BinaryTree(2, BinaryTree(3)))
        self.assertFalse(solve(root))
    
    def test_large_balanced_tree(self):
        root = BinaryTree(1,
                        BinaryTree(2, BinaryTree(4), BinaryTree(5)),
                        BinaryTree(3, BinaryTree(6), BinaryTree(7)))
        self.assertTrue(solve(root))
    
    def test_large_unbalanced_tree(self):
        root = BinaryTree(1,
                        BinaryTree(2, BinaryTree(3, BinaryTree(4, BinaryTree(5)))))
        self.assertFalse(solve(root))


if __name__ == '__main__':
    unittest.main()
