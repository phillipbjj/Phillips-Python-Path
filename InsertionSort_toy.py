"""/**
 * Insertion sort is a basic sorting algorithm.
 *
 * Insertion sort iterates over an array, growing a sorted array behind the current location.
 * It takes each element from the input and finds the spot, up to the current point,
 * where that element belongs. It does this until it gets to the end of the array.
*/"""
#The outer loop executes N−1 times, that's quite clear.
#But the number of times the inner-loop is executed depends on the input:
#In best-case scenario, the array is already sorted and (a[j] > X) is always false
#So no shifting of data is necessary and the inner loop runs in O(1),
#In worst-case scenario, the array is reverse sorted and (a[j] > X) is always true
#Insertion always occur at the front of the array and the inner loop runs in O(N).
#Thus, the best-case time is O(N × 1) = O(N) and the worst-case time is O(N × N) = O(N2).
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
"""N = len(A)
    for i in range(1, N): # O(N)
        X = A[i] # X is the item to be inserted
        j = i-1
        while j >= 0 and A[j] > X: # can be fast or slow
            A[j+1] = A[j] # make a place for X
            j -= 1
        A[j+1] = X # index j+1 is the insertion point
    return A"""

def insertionSort(array):

    for number in range(1, len(array)):
        insertionHere = array[number]
        insert = number - 1
        while insert >= 0 and array[insert] > insertionHere:
              array[insert + 1] = array[insert]
              insert -= 1
              
        array[insert + 1] = insertionHere  

    return array 
#print(insertionSort([6, 2, 10, 7]))
print(insertionSort([45, 12, 78, 23, 56, 91, 34, 8, 67, 19]))

"""This algorithm sorts the array in ascending order by repeatedly finding the minimum element 
from the unsorted part and putting it at the beginning of the sorted part.
The time complexity of this algorithm is O(n^2) where n is the number of elements in the array.
This makes it less efficient on large lists, and generally performs worse than the similar selection sort. 
However, insertion sort provides several advantages such as simple implementation, efficient for small data sets, 
more efficient in practice than most other simple quadratic algorithms 
such as selection sort or bubble sort, adaptive, stable, and in-place.
It is also used in more advanced algorithms like quicksort and shellsort as a subroutine for sorting small arrays."""