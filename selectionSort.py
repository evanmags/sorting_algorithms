def selectionSort(l: list) -> list:
  """
  consumes a list and sorts using the selection sort algorithm
  returns the sorted list
  >>> selectionSort([7, 1, 3, 5, 4, 6, 2]) -> [1, 2, 3, 4, 5, 6, 7]
  """
  newL = []

  while len(l) > 0:
    smallest = l[0]
    for item in l:
      if item < smallest:
        smallest = item
      
    l.remove(smallest)
    newL.append(smallest)
  
  l = newL

  return l

