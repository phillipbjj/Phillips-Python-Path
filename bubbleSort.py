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

def bubbleSort(array): 
    numberSpot = 0
    nextNumber = numberSpot + 1
    for number in range(len(array)):
        if array[numberSpot] > number + 1:
            array[number + 1] = numberSpot


    return array


print(bubbleSort([2, 1, 3]))
#print(bubbleSort([45, 12, 78, 23, 56, 91, 34, 8, 67, 19]))