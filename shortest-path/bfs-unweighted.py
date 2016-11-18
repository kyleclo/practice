"""

BFS finds the shortest path on Directed/Undirected (Unweighted) Graph

"""

import numpy as np
from collections import deque


def find_shortest_path_tree(index_start, graph):
    colors = ['white'] * len(graph)
    colors[index_start] = 'gray'

    distances = [float('inf')] * len(graph)
    distances[index_start] = 0

    parents = [None] * len(graph)

    candidate_queue = deque([index_start])

    while len(candidate_queue) > 0:
        index_current = candidate_queue.pop()
        colors[index_current] = 'black'

        for index_neighbor in graph[index_current]:
            if colors[index_neighbor] == 'white':
                candidate_queue.appendleft(index_neighbor)
                colors[index_neighbor] = 'gray'
                distances[index_neighbor] = distances[index_current] + 1
                parents[index_neighbor] = index_current

    return distances, parents


def get_shortest_path(parents, index_end):
    index_parent = parents[index_end]
    if index_parent is None:
        return str(index_end)
    else:
        return get_shortest_path(parents, index_parent) + ' -> ' + str(index_end)


if __name__ == '__main__':
    np.random.seed(0)

    n = 10
    graph = [list(np.random.permutation(n)[:np.random.randint(n)]) for _ in range(n)]

    for i in range(n):
        print str(i) + ': ' + str(graph[i])

    # shortest paths from vertex 0
    distances, parents = find_shortest_path_tree(index_start=0, graph=graph)
    for i in range(n):
        string = ''
        string += 'Distance: ' + str(distances[i]) + '\n'
        string += 'Shortest Path: ' + str(get_shortest_path(parents=parents, index_end=i)) + '\n'
        print string


