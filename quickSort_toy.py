def quickSort(array):
    
    low = array[0]
    high = array[-1]
    pivot = array[0]
    partition1 = []
    partitionP = []
    partition2 = []
    #indexer = array + 1
    #fried = pivot + 1
    """ for num in array:
        if array[num] < pivot:
            return quickSort(array, pivot, pivot + 1, high)
        if array[num] > pivot:
            return quickSort(array, pivot, high, pivot - 1)"""
    for increment in array:
            if increment > pivot :
                partition2.append(increment) 
            elif increment < pivot:
                partition1.append(increment) 
            else:
                partitionP.append(increment)
    """for index in array:
        indexer = index + 1
        while indexer <= high:
            if """
    
    #while unsorted <= high:
                      
    return partition2

print(quickSort([27, 38, 12, 39, 29, 16]))

"""for each (unsorted) partition
set first element as pivot
  storeIndex = pivotIndex+1
  for i = pivotIndex+1 to rightmostIndex
    if ((a[i] < a[pivot]) or (equal but 50% lucky))
      swap(i, storeIndex); ++storeIndex
  swap(pivot, storeIndex-1)"""