def quickSort(array, low = None, high = None):

    partition1 = []
    partitionP = []
    partition2 = []
    if low is None:
        low = 1
    if high is None:
        high = len(array)
    pivot = array[0]
    indexer = low
    for increment in range(low, high):
        if array[increment] > pivot:
            array[increment], array[indexer] = array[indexer], array[increment]
            #indexer = indexer + 1
            partition2.append(array[increment])
        elif array[increment] < pivot:
            #indexer, array[increment] = array[increment], indexer
            partition1.append(array[increment])     
        #else:
            #partitionP.append(increment)
    #pivot, array[indexer] = array[indexer], pivot                
    return array
print(quickSort([27, 38, 12, 39, 29, 16]))

"""for each (unsorted) partition
set low element as pivot
  storeIndex = pivotIndex+1
  for i = pivotIndex+1 to rightmostIndex
    if ((a[i] < a[pivot]) or (equal but 50% lucky))
      swap(i, storeIndex); ++storeIndex
  swap(pivot, storeIndex-1)"""

""" for num in array:
        if array[num] < pivot:
            return quickSort(array, pivot, pivot + 1, high)
        if array[num] > pivot:
            return quickSort(array, pivot, high, pivot - 1)"""