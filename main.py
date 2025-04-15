def valid_pos(new_r, new_c, size):
    return (0 <= new_c < size) and (0 <= new_r < size)


def solve(size, r_start, c_start, r_end, c_end):
    if not valid_pos(r_start, c_start, size):
        raise IndexError
    if not valid_pos(r_end, c_end, size):
        raise IndexError
    prev = {(r_start, c_start): (-1, -1)}
    que = [(r_start, c_start, 0)]
    visited = {(r_start, c_start)}
    move_list = [(2, -1), (2, 1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
    while len(que) != 0:
        node_r, node_c, depth = que.pop(0)
        if node_c == c_end and node_r == r_end:
            return depth, prev
        for mr, mc in move_list:
            new_r = node_r+mr
            new_c = node_c+mc
            if not valid_pos(new_r, new_c, size):
                continue
            if (new_r, new_c) in visited:
                continue
            visited.add(((new_r, new_c)))
            prev[(new_r, new_c)] = (node_r, node_c)
            que.append((new_r, new_c, depth+1))
    return -1


def read_input(path):
    with open(path, 'r') as file:
        size = int(file.readline().split()[0])
        r_start, c_start = map(int, file.readline().split(', ')[0:2])
        r_end, c_end = map(int, file.readline().split(', ')[0:2])
        return (size, r_start, c_start, r_end, c_end)


def main():
    path = 'input.txt'
    size, r_start, c_start, r_end, c_end = read_input(path)
    num, prev = solve(size, r_start, c_start, r_end, c_end)
    tail = (r_end, c_end)
    path = []
    while tail != (-1, -1):
        path.append(tail)
        # print(tail)
        tail = prev[tail]
    path.reverse()
    print(path)
    with open('output.txt', 'w') as file:
        file.write(str(num)+'\n')


if __name__ == '__main__':
    main()
