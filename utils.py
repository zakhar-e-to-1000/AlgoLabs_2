class Node:
    def __init__(self, val, prior):
        self.right = None
        self.left = None
        self.val = val
        self.prior = prior
        self.height = 1

    def __str__(self):
        return str(self.prior)


def print_tree(root):
    curr_level = -1
    next_level = [root.prior]
    node_que = [(root, 0, 0)]
    print_plan = []
    max_len = 0
    while len(node_que) != 0:
        node, level, right_adj = node_que.pop(0)
        if level > curr_level:
            str_level = ' '.join(map(str, next_level))
            print_plan.append(str_level)
            max_len = max(max_len, len(str_level))
            curr_level += 1
            next_level = ['.' for _ in range(2**(curr_level+1))]

        if node.left != None:
            node_que.append((node.left, level+1, 2*right_adj))
            next_level[2*right_adj] = node.left.prior
        if node.right != None:
            node_que.append((node.right, level+1, 2*right_adj+1))
            next_level[2*right_adj+1] = node.right.prior
    for string in print_plan:
        print(string.center(max_len))


if __name__ == '__main__':
    a = Node(1)
    a.right = Node(2)
    a.right.left = Node(3)
    print_tree(a)
