"""

Find next greater element in an array

e.g.  x = [3, 2, 1, 5, 4,   7,  3, 2,  6]
      y = [5, 5, 5, 7, 7, None, 6, 6, None]

-----------------------------------------------------------------

Idea:
    As we go left->right along x, we're looking for closest
    matching pair, similar to problem of parenthesis matching:

        [({[]})]  -->  toss ({[ into stack & pop when see matching ]})

    Here, we toss x[i]s into stack & pop when we see a larger element to the right.

    This is more efficient because we don't have to look for solutions while x is
    decreasing, and once x increases, that new value could be solution to multiple
    stack elements.

-------------------------------------------------------------------

Note that this is the next greater element, not greatest overall.
For example, if we do something like:

    largest = x[n-1]
    for i = (n-2),...,0:
        if x[i] < largest:
            solution[i] = largest
        else:
            solution[i] = None
            largest = x[i]

We'd get y = [7, 7, 7, 7, 7, None, 6, 6, None] instead.

"""


import numpy as np
from collections import namedtuple
Point = namedtuple(typename='Point', field_names=['index', 'value'])


def find_next_greater_element_naive(x):
    """O(n^2) time"""
    n = len(x)
    solution = [None] * n

    for i in range(n):
        j = i + 1
        while j < n:
            if x[j] > x[i]:
                solution[i] = x[j]
                break
            j += 1

    return solution


def find_next_greater_element_stack(x):
    """O(n) time using O(n) space for stack"""
    n = len(x)
    solution = [None] * n
    stack = []

    for i in range(n):

        if len(stack) == 0:
            stack.append(Point(index=i, value=x[i]))

        else:
            if stack[-1].value >= x[i]:
                stack.append(Point(index=i, value=x[i]))

            else:
                while len(stack) > 0 and stack[-1].value < x[i]:
                    solution[stack.pop().index] = x[i]
                stack.append(Point(index=i, value=x[i]))

    return solution


if __name__ == '__main__':
    np.random.seed(0)

    x = np.random.permutation(10)
    print x

    print find_next_greater_element_naive(x)
    print find_next_greater_element_stack(x)
    
    
    
