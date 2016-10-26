"""

Depth first search

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def depth_first_search_recursive(node, query, visited):
    if node.value == query:
        return True
    else:
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if depth_first_search_recursive(neighbor, query, visited):
                    return True
        return False


def depth_first_search_iterative(start_node, query):
    visited = set()
    stack = [start_node]

    while len(stack) > 0:
        node = stack.pop()

        if node.value == query:
            return True
        else:
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    return False


if __name__ == '__main__':
    n1 = Node(value=1)
    n2 = Node(value=2)
    n3 = Node(value=3)
    n4 = Node(value=4)
    n5 = Node(value=5)

    n1.neighbors.append(n2)
    n1.neighbors.append(n3)
    n1.neighbors.append(n4)

    n2.neighbors.append(n4)
    n2.neighbors.append(n5)

    n3.neighbors.append(n5)

    n4.neighbors.append(n1)

    n5.neighbors.append(n4)

    print depth_first_search_recursive(node=n1, query=1, visited=set())
    print depth_first_search_recursive(node=n1, query=2, visited=set())
    print depth_first_search_recursive(node=n1, query=3, visited=set())
    print depth_first_search_recursive(node=n1, query=4, visited=set())
    print depth_first_search_recursive(node=n1, query=5, visited=set())
    print depth_first_search_recursive(node=n1, query=6, visited=set())

    print depth_first_search_iterative(start_node=n1, query=1)
    print depth_first_search_iterative(start_node=n1, query=2)
    print depth_first_search_iterative(start_node=n1, query=3)
    print depth_first_search_iterative(start_node=n1, query=4)
    print depth_first_search_iterative(start_node=n1, query=5)
    print depth_first_search_iterative(start_node=n1, query=6)

