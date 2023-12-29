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

"""def binary_search(nums,target,low,high):
  if low > high:
    return False
  else:
    mid = (low + high)//2
    if nums[mid] == target:
      return True
    elif nums[mid] < target:
      return binary_search(nums,target,mid+1,high)
    else:
      return binary_search(nums,target,low,mid-1)
    nums = [2,5,7,11,14,21,27,30,36]
target = 27

print(binary_search(nums,target,0,len(nums)-1))
# Output: True

target = 38
print(binary_search(nums,target,0,len(nums)-1))
# Output: False """

def binarySearch(array, target):
  first = array[0]
  last = len(array) - 1
  mid = (first + last) // 2

  if array[mid] == target:
    return array.index(mid)
  elif 
        
    
  return "Null"
        
index = binarySearch([1, 2, 3, 4, 5], 4)
#index = binarySearch([1, 2, 3, 4, 5], 8)
print(index)  