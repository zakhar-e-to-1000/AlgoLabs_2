def parent(index):
    return (index-1)//2


def left_child(index):
    return index*2+1


def right_child(index):
    return index*2+2


class Heap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr)-1
        while i > 0:
            p = parent(i)
            if self.arr[p] < self.arr[i]:
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
                i = p
            else:
                break

    def heap_down(self):
        i = 0
        l = left_child(i)
        r = right_child(i)
        while l < len(self.arr):
            if r >= len(self.arr):
                if self.arr[l] > self.arr[i]:
                    self.arr[i], self.arr[l] = self.arr[l], self.arr[i]
                    i = l
                else:
                    break
                continue
            else:
                max_child = l if self.arr[l] > self.arr[r] else r
                if self.arr[max_child] > self.arr[i]:
                    self.arr[max_child], self.arr[i] = self.arr[i], self.arr[max_child]
                    i = max_child
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
