"""

Binary search

"""


def binary_search_recursive(x, query, index_start, index_end):
    if index_start <= index_end:
        index_middle = index_start + (index_end - index_start) / 2

        if x[index_middle] < query:
            return binary_search_recursive(x, query, index_middle + 1, index_end)
        elif x[index_middle] > query:
            return binary_search_recursive(x, query, index_start, index_middle - 1)
        else:
            return index_middle

    else:
        return None


def binary_search_iterative(x, query):
    index_start = 0
    index_end = len(x) - 1

    while index_start <= index_end:
        index_middle = index_start + (index_end - index_start) / 2

        if x[index_middle] < query:
            index_start = index_middle + 1
        elif x[index_middle] > query:
            index_end = index_middle - 1
        else:
            return index_middle

    return None


if __name__ == '__main__':
    x = range(10)
    print 'Sorted array: ' + str(x)
    print 'Contains 5: ' + str(binary_search_recursive(x, 5, 0, len(x) - 1))
    print 'Contains 11: ' + str(binary_search_recursive(x, 11, 0, len(x) - 1))
    print 'Contains 5: ' + str(binary_search_iterative(x, 5))
    print 'Contains 11: ' + str(binary_search_iterative(x, 11))


