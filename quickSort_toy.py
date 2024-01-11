def quickSort(array):
    
    low = array[0]
    high = array[-1]
    pivot = array[0]
    partition1 = {}
    partitionP = {}
    partition2 = {}
    #indexer = array + 1
    #fried = pivot + 1
    """ for num in array:
        if array[num] < pivot:
            return quickSort(array, pivot, pivot + 1, high)
        if array[num] > pivot:
            return quickSort(array, pivot, high, pivot - 1)"""
    for increment in array:
            if increment > pivot :
                #low += 1
                partition2[increment] = partition2.get(increment, 0) + 1
                
            elif increment < pivot:
                #high += 1
                partition1[increment] = partition1.get(increment, 0) + 1
            else:
                partitionP[increment] = partitionP.get(increment, 0) + 1
                
            
    return partitionP


print(quickSort([27, 38, 12, 39, 29, 16]))
