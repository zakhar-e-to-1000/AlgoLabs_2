from time import time


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


def solve_greedy(beers_bit: list, workers_num):
    ans = 0
    beers_bit.sort(key=lambda e: bin(e)[2:].count('1'), reverse=True)
    # print(list(map(bin, beers_bit)))
    for i, beer in enumerate(beers_bit):
        ans = ans | beer
        if bin(ans)[2:].count('1') == workers_num:
            return i+1
    return -1


def main():
    workers_num, brands_num = 0, 0
    pref_list = []
    with open('input.txt', 'r') as file:
        workers_num, brands_num = map(
            int, file.readline().rstrip('\n').split())
        pref_list = file.readline().rstrip().split()
    print(workers_num, brands_num)
    print(pref_list)

    workers_num, brands_num = 19, 19
    pref_list = []
    for wi in range(workers_num):
        pref_list.append('')
        for bi in range(brands_num):
            if wi == bi:
                pref_list[wi] += 'Y'
            else:
                pref_list[wi] += 'N'
    print(workers_num, brands_num)
    print(pref_list)

    beers = [0] * brands_num
    for wi, worker in enumerate(pref_list):
        for bi, char in enumerate(worker):
            if (char == 'Y'):
                beers[bi] = beers[bi] | (1 << wi)
    start = time()
    if min(workers_num, brands_num) > 18:
        print(solve_greedy(beers, workers_num))
    else:
        print(solve(beers, workers_num))
    end = time()
    print(end-start)


if __name__ == '__main__':
    main()
