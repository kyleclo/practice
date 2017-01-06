"""

Find median of two sorted arrays of equal length

"""

import numpy as np


def find_median_equal(x, y, start_x, end_x, start_y, end_y):
    n = end_x - start_x + 1

    # base cases
    if n == 0: return None
    if n == 1: return 0.5 * (x[start_x] + y[start_x])
    if n == 2:
        return 0.5 * (max(x[start_x], y[start_y]) + min(x[end_x], y[end_y]))

    # compute medians, check equality, subset arrays
    mx = median(x, start_x, end_x)
    my = median(y, start_y, end_y)

    if mx == my:
        return mx
    elif mx < my:
        if n % 2 != 0:
            return find_median_equal(x, y,
                                     start_x + n / 2, end_x,
                                     start_y, start_y + n / 2)
        else:
            return find_median_equal(x, y,
                                     start_x + n / 2 - 1, end_x,
                                     start_y, start_y + n / 2)
    else:
        if n % 2 != 0:
            return find_median_equal(x, y,
                                     start_x, start_x + n / 2,
                                     start_y + n / 2, end_y)
        else:
            return find_median_equal(x, y,
                                     start_x, start_x + n / 2,
                                     start_y + n / 2 - 1, end_y)


def median(array, index_start, index_end):
    n = index_end - index_start + 1
    if n % 2 != 0:
        return array[index_start + n / 2]
    return 0.5 * (array[index_start + n / 2] + array[index_start + n / 2 - 1])


if __name__ == '__main__':
    n = np.random.randint(10)
    x = sorted(np.random.randint(low=0, high=10, size=n))
    y = sorted(np.random.randint(low=0, high=10, size=n))

    print 'Array x: ' + str(x)
    print 'Array y: ' + str(y)

    if n > 0:
        print 'Median: ' + str(np.median(x + y))
    else:
        print 'Median: None'

    print 'Median: ' + str(find_median_equal(x, y, 0, n - 1, 0, n - 1))


