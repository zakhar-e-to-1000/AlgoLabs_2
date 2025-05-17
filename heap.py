def parent(index):
    return (index-1)//2


def left_child(index):
    return index*2+1


def right_child(index):
    return index*2+2


class MinHeap:
    def __init__(self, key):
        self.arr = []
        self.key = key

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr)-1
        while i > 0:
            p = parent(i)
            if self.key(self.arr[p]) > self.key(self.arr[i]):
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
                i = p
            else:
                break

    def __len__(self):
        return len(self.arr)

    def heap_down(self):
        i = 0
        l = left_child(i)
        r = right_child(i)
        while l < len(self.arr):
            if r >= len(self.arr):
                if self.key(self.arr[l]) < self.key(self.arr[i]):
                    self.arr[i], self.arr[l] = self.arr[l], self.arr[i]
                    i = l
                else:
                    break
                continue
            else:
                min_child = l if self.key(
                    self.arr[l]) < self.key(self.arr[r]) else r
                if self.key(self.arr[min_child]) < self.key(self.arr[i]):
                    self.arr[min_child], self.arr[i] = self.arr[i], self.arr[min_child]
                    i = min_child
                else:
                    break
            r = right_child(i)
            l = left_child(i)

    def deque(self):
        if (len(self.arr) == 0):
            raise IndexError
        max_el = self.arr[0]
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop()
        self.heap_down()
        return max_el

    def __str__(self):
        return str(self.arr)
