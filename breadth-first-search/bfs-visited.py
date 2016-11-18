"""

BFS on Directed/Undirected Graph represented by Adjacency List

"""

import numpy as np
from collections import deque


def bfs(query_value, graph):
    has_visited = [False] * len(graph)

    for index_vertex in range(len(graph)):
        if has_visited[index_vertex] is False:
            if bfs_util(query_value, index_vertex, graph, has_visited) is True:
                return True

    return False


def bfs_util(query_value, index_start, graph, has_visited):
    candidate_queue = deque([index_start])

    while len(candidate_queue) > 0:
        index_current = candidate_queue.pop()

        if index_current == query_value:
            return True

        if has_visited[index_current] is False:
            has_visited[index_current] = True
            for index_neighbor in graph[index_current]:
                if has_visited[index_neighbor] is False:
                    candidate_queue.appendleft(index_neighbor)

    return False


if __name__ == '__main__':
    np.random.seed(0)

    n = 10
    graph = [list(np.random.permutation(n)[:np.random.randint(n)]) for _ in range(n)]

    for i in range(n):
        print str(i) + ': ' + str(graph[i])

    print [bfs(query_value=i, graph=graph) for i in range(n + 1)]


