
class Node(object):
  def __init__(self, x):
    self.x = x
    self.left = None
    self.right = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n6.right = n7

import numpy as np
def max_depth(node):
  if node is None:
    return 0
  else:
    return np.max([max_depth(node.left), max_depth(node.right)]) + 1

print(max_depth(n1))
