
def solve(beers: list[int], workers_num):
    start = 0
    target = (1 << workers_num) - 1
    visited = {0}
    que = [(0, 0)]
    while len(que) != 0:
        node, dist = que.pop()
        if node == target:
            return dist
        for beer in beers:
            new_node = node | beer
            if new_node not in visited:
                visited.add(new_node)
                que.insert(0, (new_node, dist+1))
    return -1


def main():
    workers_num, brands_num = map(int, input().split())
    pref_list = input().split()
    beers = [0] * brands_num
    for wi, worker in enumerate(pref_list):
        for bi, char in enumerate(worker):
            if (char == 'Y'):
                beers[bi] = beers[bi] | (1 << wi)
    print(solve(beers, workers_num))


if __name__ == '__main__':
    main()
