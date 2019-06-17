def bubbleSort(l):
  """
  bubble sort algorythm

  >>> bubbleSort([5, 6, 3, 4]) -> [3, 4, 5, 6]
  """
  # assume that array is unsorted to start loop
  unsorted = True
  # number of items that will be guarenteed to be in place after next loop
  count = 1

  while count < len(l):
    # now assume list is sorted
    unsorted = False

    # loop through list looking for out of place elements
    # swap them as necessary and set flag to say that list was unsorted
    for i in range(len(l) - count):
      if l[i] > l[i+1]:
        [l[i], l[i+1]] = [l[i+1], l[i]]
        unsorted = True

    # increment
    count += 1
  return l
  
print(bubbleSort([7, 1, 2, 3, 4, 5, 6]))



