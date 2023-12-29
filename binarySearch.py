# Given a sorted list, find the index of an element
# using a binary search algorithm.
#
# Example usage:
#
# index = binarySearch([1, 2, 3, 4, 5], 4);
# print(index); // 3
# index = binarySearch([1, 2, 3, 4, 5], 8);
# print(index); // null
#def binarySearch(array, target) {
  # write your algorithm logic here
#}

def binarySearch(array, target, first = None, last = None):
  
  if first == None:
    first = 0
  if last == None:
    last = len(array) - 1

  mid = (first + last) // 2

  if array[mid] == target:
    return mid
  else:
    if array[mid] < target:
      return binarySearch(array, target, mid + 1, last)
    if array[mid] > target:
      return binarySearch(array, target, last, mid - 1) 
    
  return "Null"
        
index = binarySearch([1, 2, 3, 4, 5],  4)
print(index)  