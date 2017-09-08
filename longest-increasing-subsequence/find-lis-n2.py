"""

Find longest increasing subsequence of a sequence x

"""

import numpy as np


# note: inner loop is inefficient.  see nlogn solution.
def find_lis_n2(x):
    n = len(x)
    solutions = [[xi] for xi in x]
    lengths = [1] * n
    for i in range(1, n):
        for j in range(i):
            if x[j] < x[i] and lengths[j] + 1 > lengths[i]:
                solutions[i] = solutions[j] + [x[i]]
                lengths[i] = lengths[j] + 1
    return lengths, solutions


# # slightly optimized version
# def find_lis_n2_optim(x):
#     n = len(x)
#     solutions = [[xi] for xi in x]
#     lengths = [1] * n
#     for i in range(1, n):
#
#         index_longest = None
#         for j in range(i):
#             if x[j] < x[i] and lengths[j] + 1 > lengths[i]:
#                 index_longest = j
#                 lengths[i] = lengths[j] + 1
#
#         if index_longest is not None:
#             solutions[i] = solutions[index_longest] + [x[i]]
#
#     return lengths, solutions


if __name__ == '__main__':
    x = np.random.permutation(10)
    print 'Sequence: {}'.format(x)
    print 'Lengths: {}\nSubsequences: {}'.format(*find_lis_n2(x))

