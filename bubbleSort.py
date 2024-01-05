''' Bubble sort is the most basic sorting algorithm in all of Computer
 Sciencedom. It works by starting at the first element of an list and
 comparing it to the second element; if the first element is greater than the
 second element, it swaps the two. It then compares the second to the third,
 and the third to the fourth, and so on; in this way, the largest values
 "bubble" to the end of the list. Once it gets to the end of the list, it
 starts over and repeats the process until the list is sorted numerically.

 Implement a function that takes an list and sorts it using this technique.
 Don't use any of Python's built-in sorting functions.

 QUERY: What's the time complexity of your algorithm? If you don't already
 know, try to intuit this without consulting the Googles.

 Extra credit: Optimization time! During any given pass, if no elements are
 swapped we can assume the list is sorted and can exit the function early.
 After this optimization, what is the time complexity of your algorithm?

 Moar credits: Do you need to consider every element every time you iterate
 through the list? Make it happen, boss. Again: Has the time complexity of
 your algorithm changed?

Example usage:
bubbleSort([2, 1, 3]); # yields [1, 2, 3]
'''
# Feel free to add helper functions if needed.

#freqList[j], freqList[j + 1] = freqList[j + 1], freqList[j]
#do
#swapped = false
#  for i = 1 to indexOfLastUnsortedElement-1
#    if leftElement > rightElement
#      swap(leftElement, rightElement)
#      swapped = true; ++swapCounter
#while swapped
"""Compare a pair of adjacent items (a, b),
Swap that pair if the items are out of order (in this case, when a > b),
Repeat Step 1 and 2 until we reach the end of array
(the last pair is the (N-2)-th and (N-1)-th items as we use 0-based indexing),
By now, the largest item will be at the last position.
We then reduce N by 1 and repeat Step 1 until we have N = 1."""

"""method bubbleSort(array A, integer N) // the standard version
  for each R from N-1 down to 1 // repeat for N-1 iterations
    for each index i in [0..R-1] // the 'unsorted region', O(N)
      if A[i] > A[i+1] // these two are not in non-decreasing order
        swap(a[i], a[i+1]) // swap them in O(1)
Comparison and swap require time that is bounded by a constant, let's call it c. Then, there are two nested loops in (the standard) Bubble Sort. The outer loop runs for exactly N-1 iterations. But the inner loop runs get shorter and shorter:

When R=N-1, (N−1) iterations (of comparisons and possibly swaps),
When R=N-2, (N−2) iterations,
...,
When R=1, 1 iteration (then done).
Thus, the total number of iterations = (N−1)+(N−2)+...+1 = N*(N−1)/2 (derivation).

Total time = c*N*(N−1)/2 = O(N^2)."""

def bubbleSort(array): 
    biggestNum = 0
    nextNumber = 0
    bubbling = False
        
    for number in array[0:]:
        if number == number:
                continue
            
        if array[biggestNum] > number + 1:
                array[biggestNum] = number + 1
                biggestNum = number + 1
                nextNumber = biggestNum + 1
        elif array[biggestNum] < number + 1:
                array[biggestNum] = array[biggestNum + 1]
                biggestNum = number + 1
                nextNumber = biggestNum + 1
                
    #array[biggestNum] = array[biggestNum + 1] # = array[biggestNum]
    #while bubbling:

    return array


print(bubbleSort([2, 1, 3]))
#print(bubbleSort([45, 12, 78, 23, 56, 91, 34, 8, 67, 19]))