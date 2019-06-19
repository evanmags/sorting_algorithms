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
  
  right = quickSort(l[index + 1:]) if index != len(l) - 1 else []
  left = quickSort(l[:index]) if index != 0 else []
  
  return left + [ pivot ] + right
    