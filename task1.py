class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solve(root: BinaryTree):
    que_1 = [root.left, root.right]
    que_2 = [('left', 0), ('right', 0)]
    left_max = 0
    right_max = 0
    while len(que_1) != 0:
        node = que_1.pop(0)
        branch, depth = que_2.pop(0)
        if branch == 'left':
            left_max = max(left_max, depth)
        if branch == 'right':
            right_max = max(right_max, depth)

        for child in [node.left, node.right]:
            if (child == None):
                continue
            que_1.append(child)
            que_2.append((branch, depth+1))

    return abs(left_max-right_max) <= 1
