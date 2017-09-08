"""

Find connected components of Undirected Graph

"""

import numpy as np


def find_connected_components(graph):
    visited = [False] * len(graph)
    connected_components = []

    for index_vertex in range(len(graph)):
        if visited[index_vertex] is False:
            current_component = []
            dfs(index_vertex, graph, visited, current_component)
            connected_components.append(current_component)

    return connected_components


#  bfs would work here as well
def dfs(index_current, graph, visited, current_component):
    if visited[index_current] is False:
        visited[index_current] = True
        current_component.append(index_current)
        for index_neighbor in graph[index_current]:
            if visited[index_neighbor] is False:
                dfs(index_neighbor, graph, visited, current_component)


if __name__ == '__main__':
    np.random.seed(0)

    graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2],
             [5, 6, 7], [4, 6, 7], [4, 5, 7], [4, 5, 6],
             [9], [8]]

    for i in range(len(graph)):
        print str(i) + ': ' + str(graph[i])

    print find_connected_components(graph)


