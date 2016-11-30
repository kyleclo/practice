"""

Counting sort

"""


import numpy as np


def bucket_sort(x):

    n = len(x)
    buckets = [[] for _ in range(n)]

    for xi in x:
        buckets[int(n * xi)].append(xi)

    # worst case complexity depends on this.
    # insertion sort most common since least overhead despite O(n^2) 
    # merge sort for large bins
    for bucket in buckets:
        bucket.sort()

    out = []
    for bucket in buckets:
        out.extend(bucket)

    return out


if __name__ == '__main__':
    np.random.seed(0)
    x = np.random.uniform(size=10)
    print 'Unsorted: ' + str(x)
    print 'Sorted: ' + str(bucket_sort(x))



