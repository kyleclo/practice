"""

Topological Sort with Kahn's algorithm on Directed Acyclic Graph

"""

from collections import deque


def topological_sort(graph):
    # compute in-degrees of every vertex
    in_degrees = [0] * len(graph)
    for index_vertex in range(len(graph)):
        for index_neighbor in graph[index_vertex]:
            in_degrees[index_neighbor] += 1

    # add 0 in-degree vertices to queue (guaranteed at least one)
    candidate_queue = deque()
    for index_vertex in range(len(graph)):
        if in_degrees[index_vertex] == 0:
            candidate_queue.appendleft(index_vertex)

    # continually remove 0 in-degree vertices and their edges from graph
    finished = []
    while len(candidate_queue) > 0:
        index_current = candidate_queue.pop()
        finished.append(index_current)
        for index_neighbor in graph[index_current]:
            in_degrees[index_neighbor] += -1
            if in_degrees[index_neighbor] == 0:
                candidate_queue.appendleft(index_neighbor)

    # check for cycles
    if len(finished) < len(graph):
        return 'Cycle detected!'

    string = ''
    for vertex in finished:
        string += str(vertex) + ' -> '
    string += 'Finished'
    return string


if __name__ == '__main__':

    # without cycle
    n = 5
    graph = [[] for _ in range(n)]
    graph[0] = [2, 3]
    graph[1] = [0, 3]
    graph[2] = [4]
    graph[3] = [2, 4]

    for vertex in graph:
        print vertex

    print topological_sort(graph)

    # with cycle
    graph2 = [[i] for i in range(n)]

    for vertex in graph2:
        print vertex

    print topological_sort(graph2)


