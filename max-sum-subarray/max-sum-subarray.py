"""

Given an array, find the contiguous subarray s.t. sum of elements is maximal

"""


def find_max_sum_subarray_brute_force(x):

    max_sum, index_max_start, index_max_end = -float('inf'), None, None

    for index_start in range(len(x)):
        current_sum = 0

        for index_end in range(index_start, len(x)):
            current_sum += x[index_end]

            if current_sum > max_sum:
                max_sum, index_max_start, index_max_end = current_sum, index_start, index_end

    return x[index_max_start:(index_max_end + 1)]


def find_max_sum_subarray_divide_conquer(x, index_start, index_end):
    if index_start < index_end:
        index_middle = index_start + (index_end - index_start) / 2

        left = find_max_sum_subarray_divide_conquer(x, index_start, index_middle)
        right = find_max_sum_subarray_divide_conquer(x, index_middle + 1, index_end)
        cross = _find_max_cross_subarray(x, index_start, index_middle, index_end)

        sum_left = sum(left)
        sum_right = sum(right)
        sum_cross = sum(cross)

        if sum_left >= sum_right and sum_left >= sum_cross:
            return left
        elif sum_right >= sum_left and sum_right >= sum_cross:
            return right
        else:
            return cross

    else:
        single_value = x[index_start]
        return [single_value]


def _find_max_cross_subarray(x, index_start, index_middle, index_end):
    #  Find max subarray [?, index_middle]
    max_left, index_max_left = -float('inf'), index_middle

    sum_left = 0
    for index_left in range(index_middle, index_start - 1, -1):
        sum_left += x[index_left]

        if sum_left > max_left:
            max_left, index_max_left = sum_left, index_left

    # Find max subarray [index_middle + 1, ?]
    max_right, index_max_right = -float('inf'), index_middle + 1

    sum_right = 0
    for index_right in range(index_middle + 1, index_end + 1):
        sum_right += x[index_right]

        if sum_right > max_right:
            max_right, index_max_right = sum_right, index_right

    return x[index_max_left:(index_max_right + 1)]


def find_max_sum_subarray_dynamic_programming(x):
    max_sum, index_max_left, index_max_right = -float('inf'), None, None

    current_sum, index_left = 0, 0
    for index_right in range(len(x)):

        current_sum += x[index_right]

        #  keep track of maximal subarray ENDING at index_right
        if current_sum <= x[index_right]:
            current_sum, index_left = x[index_right], index_right

        if current_sum > max_sum:
            max_sum, index_max_left, index_max_right = current_sum, index_left, index_right

    return x[index_max_left:(index_max_right + 1)]


if __name__ == '__main__':
    x = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print 'Array: ' + str(x)
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_brute_force(x))
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_divide_conquer(x, 0, len(x) - 1))
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_dynamic_programming(x))

    x = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
    print 'Array: ' + str(x)
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_brute_force(x))
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_divide_conquer(x, 0, len(x) - 1))
    print 'Max Sum Subarray: ' + str(find_max_sum_subarray_dynamic_programming(x))


