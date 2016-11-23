"""

Counting sort

"""


import numpy as np


def counting_sort(x):
    n = len(x)
    max_value = max(x)

    counts = [0] * (max_value + 1)

    for i in range(n):
        counts[x[i]] += 1

    for i in range(1, max_value + 1):
        counts[i] += counts[i-1]

    out = [None] * n
    for i in range(n-1, -1, -1):
        out[counts[x[i]]-1] = x[i]
        counts[x[i]] += -1

    return out


def counting_sort2(x):
    n = len(x)
    max_value = max(x)

    # temp[j] stores x[i]s with integer key = j in stable order
    temp = [[] for _ in range(max_value + 1)]

    for i in range(n):
        temp[x[i]].append(x[i])

    out = []
    for i in range(max_value + 1):
        out.extend(temp[i])

    return out


if __name__ == '__main__':
    np.random.seed(0)
    x = np.random.randint(10, size=10)
    print 'Unsorted: ' + str(x)
    print 'Sorted: ' + str(counting_sort(x))
    print 'Sorted: ' + str(counting_sort2(x))


