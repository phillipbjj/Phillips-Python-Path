def quickSort(array, low = None, high = None):

    partition1 = []
    partition2 = []
    if low is None:
        low = 0
    if high is None:
        high = len(array)
    pivot = array[0]
    indexer = low - 1
    for increment in range(low, high):
        if array[increment] >= pivot:        
            partition2.append(array[increment])
        elif array[increment] < pivot:
            partition1.append(array[increment])     
    
    return partition1
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