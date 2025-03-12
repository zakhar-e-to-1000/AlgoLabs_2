class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def recursive_solve(node: BinaryTree):
    if node == None:
        return (0, True)
    l_height, l_bool = recursive_solve(node.left)
    r_height, r_bool = recursive_solve(node.right)
    if not (l_bool and r_bool):
        return (-1, False)
    if abs(l_height-r_height) > 1:
        return (-1, False)
    height = max(l_height, r_height)+1
    return (height, True)


def iterative_solve(root: BinaryTree):
    if not isinstance(root, BinaryTree):
        return True
    stack = [root]
    stack_prev = [-1]
    stack_left = [False]
    travel_map = []
    travel_prev = []
    travel_left = []
    while len(stack) != 0:
        node = stack.pop()
        prev = stack_prev.pop()
        is_left = stack_left.pop()
        travel_map.append(node.value)
        travel_prev.append(prev)
        travel_left.append(is_left)
        index = len(travel_prev)-1
        for child in (node.left, node.right):
            if child != None:
                stack.append(child)
                stack_prev.append(index)
                stack_left.append(child==node.left)
    # print(travel_map)
    # print(travel_prev)

    length = len(travel_prev)
    height = [1]*length
    balance = [0]*length
    for i in range(length-1, -1, -1):
        prev_i = travel_prev[i]
        if abs(balance[i]) > 1:
            return False
        if travel_prev[i]==-1:
            break
        if travel_left[i]:
            balance[prev_i] += height[i]
        else:
            balance[prev_i] -= height[i]
        height[prev_i] = max(height[prev_i], height[i]+1)
    return True

def solve(node):
    return iterative_solve(node)
    # return recursive_solve(node)[1]


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(3)
    root.left.left.left = BinaryTree(5)
    root.right = BinaryTree(4)
    print(iterative_solve(root))


if __name__ == '__main__':
    main()
