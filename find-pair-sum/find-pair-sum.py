"""

Find a pair of integers in an array 'x' has sum equal to 'query'

"""

import numpy as np


def find_pair_sum(x, query):
    x = np.sort(x)

    index_left = 0
    index_right = len(x) - 1

    while index_left < index_right:

        sum = x[index_left] + x[index_right]

        if sum > query:
            index_right += -1

        elif sum < query:
            index_left += 1

        else:
            return x[index_left], x[index_right]

    return None


def main():
    x = [1, 4, -3, 6, 7, -2]
    print x

    print 'Pair sums to 4: ' + str(find_pair_sum(x, 4))
    print 'Pair sums to 20: ' + str(find_pair_sum(x, 20))


if __name__ == '__main__':
    main()
