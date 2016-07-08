"""

Solving the maximal sum subarray problem using Divide and Conquer

"""

import numpy as np


def find_max_sum_subarray(x, index_start, index_end):
    if index_start < index_end:
        index_middle = index_start + (index_end - index_start) / 2

        left = find_max_sum_subarray(x, index_start, index_middle)
        right = find_max_sum_subarray(x, index_middle + 1, index_end)
        cross = find_max_cross_subarray(x, index_start, index_middle,
                                        index_end)

        sum_left = np.sum(left)
        sum_right = np.sum(right)
        sum_cross = np.sum(cross)

        if sum_left > sum_right and sum_left > sum_cross:
            return left
        elif sum_right > sum_left and sum_right > sum_cross:
            return right
        else:
            return cross

    else:
        single_value = x[index_start]
        return single_value


def find_max_cross_subarray(x, index_start, index_middle, index_end):
    #  Find max subarray [?, index_middle]
    index_max_left = index_middle
    max_left = 0
    sum_left = 0
    for index_left in range(index_middle, index_start - 1, -1):

        sum_left += x[index_left]

        if sum_left > max_left:
            max_left = sum_left
            index_max_left = index_left

    # Find max subarray [index_middle + 1, ?]
    index_max_right = index_middle + 1
    max_right = 0
    sum_right = 0
    for index_right in range(index_middle + 1, index_end + 1):

        sum_right += x[index_right]

        if sum_right > max_right:
            max_right = sum_right
            index_max_right = index_right

    return x[index_max_left:(index_max_right + 1)]


def find_max_sum_subarray_brute_force(x):
    n = len(x)
    max = 0
    index_max_start, index_max_end = None, None

    for index_start in range(n):

        sum = 0
        for index_end in range(index_start, n):

            sum += x[index_end]
            if sum > max:
                max = sum
                index_max_start = index_start
                index_max_end = index_end

    return x[index_max_start:(index_max_end + 1)]


def main():
    x = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray(x, 0, len(x) - 1))
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_brute_force(x))


if __name__ == '__main__':
    main()
