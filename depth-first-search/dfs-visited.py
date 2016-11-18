"""

Depth first search on Directed Graph represented by Adjacency List

"""

import numpy as np


def dfs(query_value, graph, mode):
    has_visited = [False] * len(graph)
    for index_vertex in range(len(graph)):
        if has_visited[index_vertex] is False:
            if mode == 'recursive':
                has_found = dfs_recursive(query_value, index_vertex, graph, has_visited)
            elif mode == 'iterative':
                has_found = dfs_iterative(query_value, index_vertex, graph)
            else:
                raise Exception
	    if has_found is True:
	        return True

    return False


def dfs_recursive(query_value, index_current, graph, has_visited):
    if index_current == query_value:
        return True

    if has_visited[index_current] is False:
        has_visited[index_current] = True
        for index_neighbor in graph[index_current]:
            if has_visited[index_neighbor] is False:
                if dfs_recursive(query_value, index_neighbor, graph, has_visited) is True:
                    return True
        return False


def dfs_iterative(query_value, index_start, graph):
    has_visited = [False] * len(graph)
    candidate_stack = [index_start]

    while len(candidate_stack) > 0:
        index_current = candidate_stack.pop()

        if index_current == query_value:
            return True

        if has_visited[index_current] is False:
            has_visited[index_current] = True
            for index_neighbor in graph[index_current]:
                if has_visited[index_neighbor] is False:
                    candidate_stack.append(index_neighbor)

    return False


if __name__ == '__main__':
    np.random.seed(0)

    n = 10
    graph = [list(np.random.permutation(n)[:np.random.randint(n)]) for _ in range(n)]

    for vertex in graph:
        print vertex

    print [dfs(query_value=i, graph=graph, mode='recursive') for i in range(n + 1)]
    print [dfs(query_value=i, graph=graph, mode='iterative') for i in range(n + 1)]


