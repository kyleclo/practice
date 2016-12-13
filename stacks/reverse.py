"""

Reverse a stack

"""

import numpy as np


def reverse_stack_iterative(stack):
    temp = []

    n = len(stack)
    for i in range(n):
        temp.append(stack.pop())

    stack.extend(temp)


def reverse_stack_recursive(stack):
    if len(stack) > 0:
        temp = stack.pop()
        reverse_stack_recursive(stack)
        _insert_at_bottom(stack, temp)


def _insert_at_bottom(stack, new):
    if len(stack) == 0:
        stack.append(new)
    else:
        temp = stack.pop()
        _insert_at_bottom(stack, new)
        stack.append(temp)


if __name__ == '__main__':
    np.random.seed(0)
    x = list(np.random.permutation(10))
    print 'Stack:' + str(x)
    
    reverse_stack_iterative(x)
    print 'Reverse: ' + str(x)
    
    reverse_stack_recursive(x)
    print 'Reverse again: ' + str(x)


