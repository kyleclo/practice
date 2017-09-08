def quick_select(x, k, index_start, index_end):
  index_kth = index_start + k - 1
  index_pivot = partition(x, index_start, index_end)
  
  if index_pivot < index_kth:
    return quick_select(x, index_kth - index_pivot, index_pivot + 1, index_end)
  
  elif index_pivot > index_kth:
    return quick_select(x, k, index_start, index_pivot - 1)
  
  else:
    return x[index_pivot]

def partition(x, index_start, index_end):
  # random
  pivot = x[index_start + (index_end - index_start) // 2]
  
  index_left = index_start
  index_right = index_end
  
  while index_left < index_right:
    
    while x[index_left] < pivot:
      index_left += 1
    
    while x[index_right] > pivot:
      index_right -= 1
      
    x[index_left], x[index_right] = x[index_right], x[index_left]
  
  # doesnt matter if left or right 
  return index_left

x = [4, 7, 9, 11, 1, 5, 2]

print([quick_select(x, k, 0, len(x) - 1) for k in range(1, len(x) + 1)])
