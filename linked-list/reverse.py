"""
reverse a linked list
"""

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
  
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

def linked_list_to_array(node):
  if node.next is None:
    return [node.val]
  return [node.val] + linked_list_to_array(node.next)
  
print(linked_list_to_array(n1))

def reverse_linked_list(node, parent):
  if node.next is not None:
    reverse_linked_list(node.next, node)
  node.next = parent
    
reverse_linked_list(n1, None)
print(linked_list_to_array(n6))

