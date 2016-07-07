"""

Bubble sort

"""

import numpy as np


def bubble_sort(x):
    for index_insert in range(len(x) - 1, 0, -1):

        is_swapped = False

        for index_candidate in range(index_insert):
            if x[index_candidate] > x[index_candidate + 1]:
                temp = x[index_candidate + 1]
                x[index_candidate + 1] = x[index_candidate]
                x[index_candidate] = temp

                is_swapped = True

        if is_swapped == False:
            break


def main():
    x = np.random.permutation(10)
    print 'Unsorted: ' + str(x)
    bubble_sort(x)
    print 'Sorted: ' + str(x)


if __name__ == '__main__':
    main()
