from utils import Node, print_tree

# RENAME 'val' to 'prior' to make it clean
# CHANGE inequalitied (FLIP THEM) BETWEEN NODE AND ITS CHILDREN


def height(node):
    if not isinstance(node, Node):
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)


def insert(root: Node, val, prior):
    node = Node(val, prior)
    if root == None:
        return node
    prev = root
    path = []
    sides = []
    while True:
        if node.prior == prev.prior:
            return root
        path.append(prev)
        if node.prior > prev.prior:
            next = prev.left
            sides.append('left')
            if next == None:
                prev.left = node
                break
            prev = next
        elif node.prior < prev.prior:
            next = prev.right
            sides.append('right')
            if next == None:
                prev.right = node
                break
            prev = next

    for i in range(len(path)-1, -1, -1):
        parent = path[i]
        parent.height = 1 + max(height(parent.left), height(parent.right))
        balance = get_balance(path[i])
        if abs(balance) <= 1:
            continue
        new_node = parent
        if balance > 1 and get_balance(parent.left) >= 0:
            new_node = rotate_right(parent)
        if balance < -1 and get_balance(parent.right) <= 0:
            new_node = rotate_left(parent)

        if balance > 1 and get_balance(parent.left) < 0:
            parent.left = rotate_left(parent.left)
            new_node = rotate_right(parent)
        if balance < -1 and get_balance(parent.right) > 0:
            parent.right = rotate_right(parent.right)
            new_node = rotate_left(parent)

        if i <= 0:
            root = new_node
        else:
            granny = path[i-1]
            if sides[i-1] == 'right':
                granny.right = new_node
            else:
                granny.left = new_node
    return root


def delete_leftmost(root):
    if root.left == None:
        return root.right, root.val
    parents = [root]
    node = root.left
    while node.left != None:
        parents.append(node)
        node = node.left
    ans = node.val
    parents[-1].left = node.right

    for i in range(len(parents)-1, -1, -1):
        parent = parents[i]
        parent.height = 1 + max(height(parent.left), height(parent.right))
        balance = get_balance(parents[i])
        if abs(balance) <= 1:
            continue
        new_node = parent
        if balance > 1 and get_balance(parent.left) >= 0:
            new_node = rotate_right(parent)
        if balance < -1 and get_balance(parent.right) <= 0:
            new_node = rotate_left(parent)

        if balance > 1 and get_balance(parent.left) < 0:
            parent.left = rotate_left(parent.left)
            new_node = rotate_right(parent)
        if balance < -1 and get_balance(parent.right) > 0:
            parent.right = rotate_right(parent.right)
            new_node = rotate_left(parent)

        if i <= 0:
            root = new_node
        else:
            granny = parents[i-1]
            granny.left = new_node
    return root, ans


def rotate_right(node):
    other = node.left
    transfer = other.right
    other.right = node
    node.left = transfer

    node.height = 1 + max(height(node.left), height(node.right))
    other.height = 1 + max(height(other.left), height(other.right))
    return other


def rotate_left(node):
    other = node.right
    transfer = other.left
    other.left = node
    node.right = transfer

    node.height = 1 + max(height(node.left), height(node.right))
    other.height = 1 + max(height(other.left), height(other.right))
    return other


class AWLqueue:
    def __init__(self):
        self.root = None

    def insert(self, val, prior):
        self.root = insert(self.root, val, prior)

    def pop(self):
        self.root, ans = delete_leftmost(self.root)
        return ans


def main():

    que = AWLqueue()
    for i in range(1, 15):
        que.insert(i, i)
    for _ in range(1, 15):
        print(que.pop())
    print()


if __name__ == '__main__':
    main()
