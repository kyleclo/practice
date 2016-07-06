"""

Merge sort

"""

import numpy as np


def merge_sort(x, index_start, index_end):
    if index_start < index_end:
        index_middle = index_start + (index_end - index_start) / 2
        merge_sort(x, index_start, index_middle)
        merge_sort(x, index_middle + 1, index_end)
        merge(x, index_start, index_middle, index_end)


def merge(x, index_start, index_middle, index_end):
    n = index_end - index_start + 1
    temp = [None] * n

    index_temp = 0
    index_left = index_start
    index_right = index_middle + 1

    while index_left <= index_middle and index_right <= index_end:

        if x[index_left] <= x[index_right]:
            temp[index_temp] = x[index_left]
            index_left += 1
        else:
            temp[index_temp] = x[index_right]
            index_right += 1

        index_temp += 1

    while index_left <= index_middle:
        temp[index_temp] = x[index_left]
        index_left += 1
        index_temp += 1

    while index_right <= index_end:
        temp[index_temp] = x[index_right]
        index_right += 1
        index_temp += 1

    for i in range(n):
        x[index_start + i] = temp[i]


def main():
    x = np.random.permutation(10)
    print 'Unsorted: ' + str(x)
    merge_sort(x, 0, len(x) - 1)
    print 'Sorted: ' + str(x)


if __name__ == '__main__':
    main()
