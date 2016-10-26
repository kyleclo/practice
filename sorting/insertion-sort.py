"""

Insertion sort

"""

import numpy as np


def insertion_sort(x):
    for index_candidate in range(2, len(x)):

        candidate = x[index_candidate]
        index_insert = index_candidate - 1

        while index_insert >= 0 and x[index_insert] > candidate:
            x[index_insert + 1] = x[index_insert]
            index_insert += -1

        x[index_insert + 1] = candidate


def main():
    x = np.random.permutation(10)
    print 'Unsorted: ' + str(x)
    insertion_sort(x)
    print 'Sorted: ' + str(x)


if __name__ == '__main__':
    main()
