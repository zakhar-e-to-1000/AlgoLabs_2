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


def inorder(root):
    if (root == None):
        return
    inorder(root.left)
    print(root, end=' ')
    inorder(root.right)


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


def find_by(root, prior):
    prev = root
    while True:
        if prior == prev.prior:
            break
        if prior > prev.prior:
            next = prev.left
            if next == None:
                return None
            prev = next
        elif prior < prev.prior:
            next = prev.right
            if next == None:
                return None
            prev = next
    return prev.val


def delete_specific(root, prior):
    prev = root
    path = []
    sides = []
    while True:
        if prior == prev.prior:
            break
        path.append(prev)
        if prior > prev.prior:
            next = prev.left
            sides.append('left')
            if next == None:
                return root
            prev = next
        elif prior < prev.prior:
            next = prev.right
            sides.append('right')
            if next == None:
                return root
            prev = next
    node = prev
    granny = path[-1]
    if node.left == None:
        vars(granny)[sides[-1]] = node.right
        node = node.right
    if node.right == None:
        vars(granny)[sides[-1]] = node.left
        node = node.left
    else:
        node.right, node.val, node.prior = delete_leftmost(node.right)
    path.append(node)
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


def find_leftmost(root):
    if root.left == None:
        return root, None
    prev = root
    node = root.left
    while node.left != None:
        prev = node
        node = node.left
    return node, prev


def delete_leftmost(root):
    if root.left == None:
        return root.right, root.val, root.prior
    parents = [root]
    node = root.left
    while node.left != None:
        parents.append(node)
        node = node.left
    ans = node.val
    ans_prior = node.prior
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
    return root, ans, ans_prior


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
        self.root, ans, ans_prior = delete_leftmost(self.root)
        return ans

    def print(self):
        inorder(self.root)


class UserDatabase:
    def __init__(self):
        self.root = None

    def insert(self, id, username):
        self.root = insert(self.root, username, id)

    def delete_specific(self, id):
        self.root = delete_specific(self.root, id)

    def find(self, id):
        return find_by(self.root, id)

    def print(self):
        inorder(self.root)


def main():
    lis = [50, 9, 14, 12, 19, 76, 54, 72, 67, 17, 23]
    lis_b = [(2278, 'Alice'), (8762, 'Bob'), (9847, 'Charlie'), (2121, 'David'), (5956, 'Emma'),
             (9376, 'Frank'), (9199, 'Grace'), (5786, 'Hannah'), (4620, 'Ian'), (2256, 'Jack')]
    lis.sort()
    lis.reverse()
    que = UserDatabase()
    for id, name in lis_b:
        que.insert(id, name)
        print_tree(que.root)
        print()
    print(que.find(9376))
    que.delete_specific(2121)
    print_tree(que.root)


if __name__ == '__main__':
    main()
