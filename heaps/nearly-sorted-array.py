"""

Sort a nearly-sorted array (each element index off by at most k)

"""


class BinaryMinHeap:
    def __init__(self, list_of_values):
        self.x = list(list_of_values)
        for i in range(len(self.x) / 2, -1, -1):
            BinaryMinHeap.min_heapify(self.x, i)

    def extract_min(self):
        if len(self.x) > 0:
            self.x[0], self.x[-1] = self.x[-1], self.x[0]
            out = self.x.pop()
            BinaryMinHeap.min_heapify(self.x, 0)
            return out

    def insert(self, new_value):
        index_new = len(self.x)
        self.x.append(float('inf'))
        self.decrease_value(index_new, new_value)

    def delete(self, index_delete):
        self.decrease_value(index_delete, -float('inf'))
        self.extract_min()

    def decrease_value(self, index_current, current_value):
        if current_value < self.x[index_current]:
            self.x[index_current] = current_value
            while index_current > 0:
                index_parent = BinaryMinHeap.parent(index_current)
                if self.x[index_current] >= self.x[index_parent]:
                    break
                else:
                    self.x[index_current], self.x[index_parent] = self.x[index_parent], self.x[index_current]
                    index_current = index_parent

    @staticmethod
    def min_heapify(x, index_current):
        n = len(x)
        index_left = BinaryMinHeap.left(index_current)
        index_right = BinaryMinHeap.right(index_current)

        # check if left child is smaller
        if index_left < n and x[index_left] < x[index_current]:
            index_smallest = index_left
        else:
            index_smallest = index_current

        # check if right child is smaller
        if index_right < n and x[index_right] < x[index_smallest]:
            index_smallest = index_right

        # correct mistake if left or right child is smaller
        if index_smallest != index_current:
            x[index_smallest], x[index_current] = x[index_current], x[index_smallest]
            BinaryMinHeap.min_heapify(x, index_smallest)

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * (index + 1)

    @staticmethod
    def parent(index):
        return (index - 1) / 2


def sort_nearly_sorted_array(x, k):
    n = len(x)
    solution = []

    # toss first k+1 into a heap
    heap = BinaryMinHeap(x[:k+1])

    # pop min & insert new value
    for i in range(k+1,n):
        solution.append(heap.extract_min())
        heap.insert(x[i])

    # pop remaining
    while len(heap.x) > 0:
        solution.append(heap.extract_min())

    return solution


if __name__ == '__main__':
    x = [2, 3, 1, 5, 6, 4]
    print 'Nearly Sorted Array (k=2): ' + str(x)
    print 'Sorted: ' + str(sort_nearly_sorted_array(x=x, k=2))



