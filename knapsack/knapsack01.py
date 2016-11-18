"""

0-1 Knapsack problem

Let N = total number of items and W = max weight allowed

"""

import numpy as np


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def knapsack_01_recursive(N, W, items):
    if N == 0 or W == 0:
        return 0

    index_current_item = N - 1
    if items[index_current_item].weight > W:
        return knapsack_01_recursive(N - 1, W, items)
    else:
        remaining_weight = W - items[index_current_item].weight
        return max(knapsack_01_recursive(N - 1, W, items),
                   items[index_current_item].value + knapsack_01_recursive(N - 1, remaining_weight, items))


def knapsack_01_dynamic(items, W):
    N = len(items)
    matrix = np.zeros([N + 1, W + 1], dtype=int)

    for n in range(1, N + 1):
        index_current_item = n - 1

        for w in range(1, W + 1):
            if items[index_current_item].weight > w:
                matrix[n, w] = matrix[n - 1, w]
            else:
                remaining_weight = w - items[index_current_item].weight
                matrix[n, w] = max(matrix[n - 1, w],
                                  items[index_current_item].value + matrix[n - 1, remaining_weight])
                # optional: if index_current_item chosen, record it

    return matrix


def get_optimal_items(matrix, items):
    optimal_items = []
    n = matrix.shape[0] - 1
    w = matrix.shape[1] - 1

    while n > 0:
        if matrix[n, w] > matrix[n - 1, w]:
            index_current_item = n - 1
            optimal_items.append(items[index_current_item])
            w += -items[index_current_item].weight
        n += -1

    optimal_items.reverse()

    return optimal_items


if __name__ == '__main__':
    items = [Item(value=1, weight=1),
             Item(value=4, weight=3),
             Item(value=5, weight=4),
             Item(value=7, weight=5)]
    max_weight = 7

    print knapsack_01_recursive(N=len(items), W=max_weight, items=items)

    matrix = knapsack_01_dynamic(items, max_weight)
    print matrix
    print [(item.value, item.weight) for item in get_optimal_items(matrix=matrix, items=items)]
