def insertionSort(l):
  index = 1

  while index < len(l):
    for i in range(index):
      loop += 1
      if l[index] < l[i]:
        item = l.pop(index)
        l.insert(i, item)
        break

    index += 1

  return l
