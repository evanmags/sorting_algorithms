def selectionSort(l):
  newL = []

  while len(l) > 0:
    smallest = l[0]
    for item in l:
      if item < smallest:
        smallest = item
      
    l.remove(smallest)
    newL.append(smallest)
  
  return newL

print(selectionSort([7, 1, 2, 3, 4, 5, 6]))