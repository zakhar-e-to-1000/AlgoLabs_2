class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def recursive_solve(node: BinaryTree):
    if node == None:
        return (0, True)
    l_height, l_bool= recursive_solve(node.left)
    r_height, r_bool = recursive_solve(node.right)
    if not (l_bool and r_bool):
        return (0, False)
    if abs(l_height-r_height)>1:
        return (0, False)
    height = max(l_height, r_height)+1
    return (height, True)

def solve(node):
    return recursive_solve(node)[1]