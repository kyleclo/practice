
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
n3.left = n6
n3.right = n7

def dfs_recursive(node, out):
  if node is not None:
    out.append(node.x)
    dfs_recursive(node.left, out)
    dfs_recursive(node.right, out)

def dfs_iterative(start):
  out = []
  stack = [start]
  while len(stack) > 0:
    current = stack.pop()
    if current is not None:
      out.append(current.x)
      stack.append(current.right)
      stack.append(current.left)
  return out

from collections import deque
def bfs(start):
  out = []
  queue = deque([start])
  while len(queue) > 0:
    current = queue.pop()
    if current is not None:
      out.append(current.x)
      queue.appendleft(current.left)
      queue.appendleft(current.right)
  return out

def inorder(node, out):
  """Useful for traversing BST from min to max"""
  if node is not None:
    inorder(node.left, out)
    out.append(node.x)
    inorder(node.right, out)

def preorder(node, out):
  """Useful for copying tree"""
  if node is not None:
    out.append(node.x)
    preorder(node.left, out)
    preorder(node.right, out)

def postorder(node, out):
  """Useful for deleting tree"""
  if node is not None:
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.x)

out = []
dfs_recursive(n1, out)
print('DFS recursive: {}'.format(out))

print('DFS iterative: {}'.format(dfs_iterative(n1)))

print('BFS: {}'.format(bfs(n1)))

out = []
inorder(n1, out)
print('Inorder: {}'.format(out))

out = []
preorder(n1, out)
print('Preorder: {}'.format(out))

out = []
postorder(n1, out)
print('Postorder: {}'.format(out))


