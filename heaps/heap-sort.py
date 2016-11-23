"""

Heap sort

"""

import numpy as np


class BinaryMaxHeap:
    def __init__(self, list_of_values):
        self.x = list(list_of_values)
        for i in range(len(self.x) / 2, -1, -1):
            BinaryMaxHeap.max_heapify(self.x, i)

    def extract_max(self):
        if len(self.x) > 0:
            self.x[0], self.x[-1] = self.x[-1], self.x[0]
            out = self.x.pop()
            BinaryMaxHeap.max_heapify(self.x, 0)
            return out

    def insert(self, new_value):
        index_new = len(self.x)
        self.x.append(-float('inf'))
        self.increase_value(index_new, new_value)

    def delete(self, index_delete):
        self.increase_value(index_delete, float('inf'))
        self.extract_max()

    def increase_value(self, index_current, current_value):
        if current_value > self.x[index_current]:
            self.x[index_current] = current_value
            while index_current > 0:
                index_parent = BinaryMaxHeap.parent(index_current)
                if self.x[index_current] <= self.x[index_parent]:
                    break
                else:
                    self.x[index_current], self.x[index_parent] = self.x[index_parent], self.x[index_current]
                    index_current = index_parent

    def sort(self):
        """Continually swap max & last elements, pop, and remake heap"""
        out = []
        while len(self.x) > 0:
            self.x[0], self.x[-1] = self.x[-1], self.x[0]
            out.append(self.x.pop())
            BinaryMaxHeap.max_heapify(self.x, 0)

        return out


    @staticmethod
    def max_heapify(x, index_current):
        n = len(x)
        index_left = BinaryMaxHeap.left(index_current)
        index_right = BinaryMaxHeap.right(index_current)

        # check if left child is larger
        if index_left < n and x[index_left] > x[index_current]:
            index_largest = index_left
        else:
            index_largest = index_current

        # check if right child is larger
        if index_right < n and x[index_right] > x[index_largest]:
            index_largest = index_right

        # correct mistake if left or right child is larger
        if index_largest != index_current:
            x[index_largest], x[index_current] = x[index_current], x[index_largest]
            BinaryMaxHeap.max_heapify(x, index_largest)

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * (index + 1)

    @staticmethod
    def parent(index):
        return (index - 1) / 2


if __name__ == '__main__':
    np.random.seed(0)
    x = np.random.permutation(10)
    print 'Array: ' + str(x)

    # turn into max-heap
    heap = BinaryMaxHeap(x)
    print 'Heap: ' + str(heap.x)

    # sort
    print 'Sort: ' + str(heap.sort())




