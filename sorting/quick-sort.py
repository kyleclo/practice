"""

Quick sort

"""

import numpy as np


def quick_sort(x, index_start, index_end):

    if index_start < index_end:

        pivot = np.random.choice(x)
        index_left = index_start
        index_right = index_end

        while index_left <= index_right:

            while x[index_left] < pivot:
                index_left += 1

            while x[index_right] > pivot:
                index_right += -1

            if index_left <= index_right:
                x[index_right], x[index_left] = x[index_left], x[index_right]
                index_left += 1
                index_right += -1

        quick_sort(x, index_start, index_right)
        quick_sort(x, index_left, index_end)


def main():
    x = np.random.permutation(10)
    print 'Unsorted: ' + str(x)
    quick_sort(x, index_start=0, index_end=len(x)-1)
    print 'Sorted: ' + str(x)


if __name__ == '__main__':
    main()