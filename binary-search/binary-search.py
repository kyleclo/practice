"""

Binary search

"""

import numpy as np


def binary_search(x, query, index_start, index_end):
    if index_start <= index_end:
        index_middle = index_start + (index_end - index_start) / 2

        if x[index_middle] < query:
            return binary_search(x, query, index_middle + 1, index_end)
        elif x[index_middle] > query:
            return binary_search(x, query, index_start, index_middle - 1)
        else:
            return index_middle

    else:
        return None


def main():
    x = range(10)
    print x
    print 'Contains 5: ' + str(binary_search(x, 5, 0, len(x) - 1))
    print 'Contains 11: ' + str(binary_search(x, 11, 0, len(x) - 1))


if __name__ == '__main__':
    main()
