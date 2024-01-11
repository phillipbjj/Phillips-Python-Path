def quickSort(array, low = None, high = None):
    if low is None:
        low = array[0]
    if high is None:
        high = array[-1]
    pivot = array[0]
    partition1 = {}
    partition2 = {}
    
    for unsorted in array:
        indexer = unsorted
        while indexer <= high:
            indexer += 1
        if unsorted > pivot:
            partition2.get(unsorted, 0) + 1
        elif unsorted < pivot:
            partition1.get(unsorted, 0) + 1
        else:
            
        
        

   







    return low


print(quickSort([27, 38, 12, 39, 29, 16]))