"""

BFS on Directed/Undirected Graph represented by Adjacency List

"""

import numpy as np


def dfs(query_value, graph):
    # white = unvisited
    colors = ['white'] * len(graph)

    for index_vertex in range(len(graph)):
        if colors[index_vertex] == 'white':
            if dfs_util(query_value, index_vertex, graph, colors) is True:
                return True

    return False


def dfs_util(query_value, index_start, graph, colors):
    # gray = pending in stack
    candidate_stack = [index_start]
    colors[index_start] = 'gray'

    while len(candidate_stack) > 0:
        index_current = candidate_stack.pop()

        if index_current == query_value:
            return True

        colors[index_current] = 'black'
        for index_neighbor in graph[index_current]:
            if colors[index_neighbor] == 'white':
                candidate_stack.append(index_neighbor)
                colors[index_neighbor] = 'gray'

    return False


if __name__ == '__main__':
    np.random.seed(0)

    n = 10
    graph = [list(np.random.permutation(n)[:np.random.randint(n)]) for _ in range(n)]

    for i in range(n):
        print str(i) + ': ' + str(graph[i])

    print [dfs(query_value=i, graph=graph) for i in range(n + 1)]


