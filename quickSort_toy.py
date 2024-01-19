def quickSort(array, low = None, high = None):
    
    if low is None:
        low = 0
    if high is None:
        high = len(array)
    pivot = low
    storageIndex = pivot + 1

    if low < high:
        for increment in range(low, high):
            if array[increment] < array[pivot]:  
                array[increment], array[storageIndex] = array[storageIndex], array[increment]
                storageIndex += 1         
        array[pivot], array[storageIndex - 1] = array[storageIndex - 1], array[pivot]
        quickSort(array, low, storageIndex - 1)
        quickSort(array, storageIndex, high)
  
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