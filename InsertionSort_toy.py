"""/**
 * Insertion sort is a basic sorting algorithm.
 *
 * Insertion sort iterates over an array, growing a sorted array behind the current location.
 * It takes each element from the input and finds the spot, up to the current point,
 * where that element belongs. It does this until it gets to the end of the array.
*/"""
"""method insertionSort(array A[], integer N)
  for i in [1..N-1] // O(N)
    let X be A[i] // X is the next item to be inserted into A[0..i-1]
    for j from i-1 down to 0 // this loop can be fast or slow
      if A[j] > X
        A[j+1] = A[j] // make a place for X
      else
        break
    A[j+1] = X // insert X at index j+1"""  
"""mark first element as sorted
for each unsorted element X
  'extract' the element X
  for j = lastSortedIndex down to 0
    if current element j > X
      move sorted element to the right by 1
    break loop and insert X here  """  

def insertionSort(array):
    
    for number in range(len(array)):
        insertionHere = array[0]
        for insert in range(0, len(array) - number - 1):
            if array[insert] > insertionHere:
                array[insert + 1] = array[insert]
            elif array[insert] < insertionHere:
                array[insert] = array[insert + 1]
            #else:
                #break
        insertionHere = array[insert + 1]

    return array
print(insertionSort([6, 2, 10, 7]))
#print(insertionSort([45, 12, 78, 23, 56, 91, 34, 8, 67, 19]))