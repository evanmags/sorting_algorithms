import random

def quickSort(l):
  pivot = l[0]
  index = 0

  enum = enumerate(l)
  for i, item in enum:
    # smaller and to the right
    if item < pivot and i > index:
      l.pop(i)
      l.insert(0, item)
      index += 1
    
    # larger and to the left
    if item > pivot and i < index:
      l.pop(i)
      l.append(item)
      index -= 1
  
  right = []
  left = []

  if index != len(l) - 1:
    right = quickSort(l[index + 1:])
  if index != 0:
    left = quickSort(l[:index])
  
  return left + [ pivot ] + right


l = []
for i in range(10000):
  l.append(random.randint(0, 10000))

print(quickSort(l))
    