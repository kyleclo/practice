"""

Print elements of a matrix in a spiral order (clockwise)

"""

import numpy as np


def spiral(M, index_top, index_bottom, index_left, index_right, start):
    if index_top > index_bottom or index_left > index_right:
        return ''

    else:
        s = ''

        if start == 'topleft':
            for j in range(index_left, index_right + 1):
                s += str(M[index_top, j]) + ' '
            return s + spiral(M, index_top + 1, index_bottom,
                              index_left, index_right, 'topright')

        elif start == 'topright':
            for i in range(index_top, index_bottom + 1):
                s += str(M[i, index_right]) + ' '
            return s + spiral(M, index_top, index_bottom,
                              index_left, index_right - 1, 'bottomright')

        elif start == 'bottomright':
            for j in range(index_right, index_left - 1, -1):
                s += str(M[index_bottom, j]) + ' '
            return s + spiral(M, index_top, index_bottom - 1,
                              index_left, index_right, 'bottomleft')

        elif start == 'bottomleft':
            for i in range(index_bottom, index_top - 1, -1):
                s += str(M[i, index_left]) + ' '
            return s + spiral(M, index_top, index_bottom,
                              index_left + 1, index_right, 'topleft')

        else:
            raise Exception


if __name__ == '__main__':
    m, n = np.random.randint(low=1, high=10, size=2)

    M = np.arange(start=1, stop=m * n + 1).reshape([m, n])

    print 'Matrix: \n' + str(M) + '\n'

    print 'Spiral: ' + spiral(M=M, index_top=0, index_bottom=m - 1,
                              index_left=0, index_right=n - 1, start='topleft')

