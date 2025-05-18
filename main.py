from math import hypot


def rope(width, h1, h2):
    return hypot(width, h1-h2)


def solve(width: int, heights: list[int]):
    n = len(heights)
    prev = [0.0] * (heights[0]+1)
    for i in range(1, n):
        next = [0.0] * (heights[i]+1)
        for h1 in range(1, heights[i]+1):
            for h2 in range(1, heights[i-1]+1):
                cand = prev[h2]+rope(width, h1, h2)
                next[h1] = max(next[h1], cand)
        prev = next.copy()
    return max(prev)


width = int(input())
heights = [int(s) for s in input().split()]
print(heights)
print(solve(width, heights))
