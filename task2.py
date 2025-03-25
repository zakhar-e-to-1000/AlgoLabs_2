from task1 import BinaryTree

file = open('text.txt', 'r')
root = BinaryTree(file.readline())
level = [root]
next_level = []
while True:
    string = file.readline()
    if string=='':
        break
    nodes = string.split()
    for i in range(len(level)):
        left = BinaryTree(nodes[i*2]) if nodes[i*2]!='0' else None
        right = BinaryTree(nodes[i*2+1]) if nodes[i*2+1]!='0' else None
        next_level.append(left)
        next_level.append(right)
        if level[i]==None:
            continue
        level[i].left = left
        level[i].right = right
    level = next_level.copy()
    print([node.value if node is not None else None for node in level])
    next_level = []

file.close()
print(root.right)