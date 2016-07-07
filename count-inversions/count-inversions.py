"""

Count number of inversions in an array.

e.g. [1, 3, 2, 5, 4] has inversions 3-2, 5-4

"""


def sort_count_inversions(x, index_start, index_end):
    if index_start < index_end:
        index_middle = index_start + (index_end - index_start) / 2
        count_left = sort_count_inversions(x, index_start, index_middle)
        count_right = sort_count_inversions(x, index_middle + 1, index_end)
        count_cross = merge_count_inversions(x, index_start, index_middle,
                                             index_end)
        return count_left + count_right + count_cross
    else:
        return 0


def merge_count_inversions(x, index_start, index_middle, index_end):
    n = index_end - index_start + 1
    temp = [0] * n

    index_temp = 0
    index_left = index_start
    index_right = index_middle + 1

    count = 0

    while index_left <= index_middle and index_right <= index_end:

        if x[index_left] <= x[index_right]:
            temp[index_temp] = x[index_left]
            index_left += 1
        else:
            temp[index_temp] = x[index_right]
            index_right += 1
            count += index_middle - index_left + 1

        index_temp += 1

    while index_left <= index_middle:
        temp[index_temp] = x[index_left]
        index_left += 1

    while index_right <= index_end:
        temp[index_temp] = x[index_right]
        index_right += 1

    for i in range(n):
        x[index_start + i] = temp[i]

    return count


def main():
    x = [2, 5, 3, 6, 1, 4]
    print x
    print 'Num Inversions: ' + str(sort_count_inversions(x, 0, len(x) - 1))


if __name__ == '__main__':
    main()
