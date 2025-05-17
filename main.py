from heap import MinHeap
import random


def solve(pairs, m):
    edges = []
    adj_list = dict()
    total_cost = 0
    for a, b, dist in pairs:
        adj_list.setdefault(a, []).append((b, dist))
        adj_list.setdefault(b, []).append((a, dist))
    s = pairs[0][0]
    que = MinHeap(lambda e: e[1])
    que.insert((s, 0, (s, s)))
    visited = set()
    while len(que) != 0:
        s, cost, edge = que.deque()
        if s in visited:
            continue
        total_cost += cost
        edges.append(edge)
        visited.add(s)
        for neigh, dist in adj_list[s]:
            if neigh not in visited:
                que.insert((neigh, dist, (s, neigh)))
    return total_cost, edges


def main():
    h = MinHeap()
    for i in range(20):
        h.insert(random.randint(1, 20))
    print(h)
    for i in range(20):
        print(h.deque())


if __name__ == "__main__":
    main()
