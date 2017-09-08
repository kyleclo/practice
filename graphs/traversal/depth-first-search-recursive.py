"""

DFS on Directed/Undirected Graph represented by Adjacency List

"""

import numpy as np


def dfs_all(graph):
    for index_start in range(len(graph)):
        # white = unvisited
        colors = ['white'] * len(graph)
        colors[index_start] = 'grey'
        parents = [None] * len(graph)
        path = []
        dfs_util(index_start, graph, colors, parents, path)
        print 'Source: ' + str(index_start)
        print 'Path: ' + str(path) + '\n'


def dfs_util(index_current, graph, colors, parents, path):
    path.append(index_current)

    # grey = pending
    if colors[index_current] == 'grey':
        for index_neighbor in graph[index_current]:
            if colors[index_neighbor] == 'white':
                colors[index_neighbor] = 'grey'
                parents[index_neighbor] = index_current
                dfs_util(index_neighbor, graph, colors, parents, path)

    # black = visited
    colors[index_current] = 'black'
    

if __name__ == '__main__':
    np.random.seed(0)

    n = 10
    graph = [list(np.random.permutation(n)[:np.random.randint(n)]) for _ in range(n)]

    for vertex in graph:
        print vertex

    dfs_all(graph)


