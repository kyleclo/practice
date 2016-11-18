"""

Topological Sort with Recursive DFS on Directed Acyclic Graph

"""

import numpy as np


def topological_sort(graph):
    has_visited = [False] * len(graph)
    finished_stack = []

    for index_vertex in range(len(graph)):
        if has_visited[index_vertex] is False:
            dfs_recursive(index_vertex, graph, has_visited, finished_stack)

    finished_stack.reverse()

    string = ''
    for vertex in finished_stack:
        string += str(vertex) + ' -> '
    string += 'Finished'
    return string


def dfs_recursive(index_current, graph, has_visited, finished_stack):
    if has_visited[index_current] is False:
        has_visited[index_current] = True
        for index_neighbor in graph[index_current]:
            if has_visited[index_neighbor] is False:
                dfs_recursive(index_neighbor, graph, has_visited, finished_stack)

        finished_stack.append(index_current)


if __name__ == '__main__':
    np.random.seed(0)

    n = 5
    graph = [[] for _ in range(n)]
    graph[0] = [2, 3]
    graph[1] = [0, 3]
    graph[2] = [4]
    graph[3] = [2, 4]

    for vertex in graph:
        print vertex

    print topological_sort(graph)


