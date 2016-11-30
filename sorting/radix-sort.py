"""

Counting sort

"""


import numpy as np


def radix_sort(x):
    # digits can take value 0, 1, ..., 9
    num_digit_values = 10

    # find number of times execute counting sort
    num_digits = 1
    while max(x) / num_digit_values ** num_digits > 1:
        num_digits += 1

    for digit in range(num_digits):
        bins = [[] for _ in range(num_digit_values)]

        # place entire x[i] value into corresponding bin based on x[i]'s digit
        for xi in x:
            bins[(xi / num_digit_values ** digit) % num_digit_values].append(xi)

        # reassign 'x' to new array & write sorted x[i]'s
        x = []
        for bin in bins:
            x.extend(bin)

    return x


if __name__ == '__main__':
    np.random.seed(0)
    x = np.random.randint(1000, size=10)
    print 'Unsorted: ' + str(x)
    print 'Sorted: ' + str(radix_sort(x))



