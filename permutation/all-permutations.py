#
#  Return a list of all permutations of input list
#

def all_permute(x, out, index_start, index_end):
  if index_start == index_end:
    out.append(x)
  else:
    for i in range(index_start, index_end + 1):
      y = [xi for xi in x]
      y[index_start], y[i] = y[i], y[index_start]
      all_permute(y, out, index_start + 1, index_end)

x = [1, 2, 3, 4, 5]
out = []
all_permute(x, out, 0, 4)

for i in range(len(out)):
  print(out[i])
print(len(out))
