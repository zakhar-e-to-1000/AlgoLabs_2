from heap import Heap
import random


def main():
    h = Heap()
    for i in range(20):
        h.insert(random.randint(1, 20))
    print(h)
    for i in range(20):
        print(h.deque())


if __name__ == "__main__":
    main()
