def quickSort(array, low = None, high = None):
    
    if low is None:
        low = 0
    if high is None:
        high = len(array)
    pivot = low
    storageIndex = pivot + 1
    for increment in range(low, high):
        if array[increment] < array[pivot]:  
            array[increment], array[storageIndex] = array[storageIndex], array[increment]
            storageIndex += 1          
    array[pivot], array[storageIndex - 1] = array[storageIndex - 1], array[pivot]
    
    if low < high:
        pivot = array[0]
        quickSort(array, pivot + 1, high)
        quickSort(array, high, pivot - 1)
    """for increment in range(low, high):
        if array[increment] < array[pivot]:
            array[increment], array[increment + 1] = array[increment + 1], array[increment]
            return quickSort(array, pivot, pivot + 1, high)
        elif array[increment] > array[pivot]:
            #array[increment], array[increment + 1] = array[increment + 1], array[increment]
             return quickSort(array, pivot, high, pivot - 1)"""
    
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