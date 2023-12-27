"""# Given a sorted list, find the index of an element
# using a binary search algorithm.
#
# Example usage:
#
# index = binarySearch([1, 2, 3, 4, 5], 4);
# print(index); // 3
# index = binarySearch([1, 2, 3, 4, 5], 8);
# print(index); // null


def binarySearch(array, target) {
  # write your algorithm logic here
}"""

def binarySearch(array, target):
    for number in array:
        if number == target:
            return array.index(number)
        
    
    return "Null"
        
index = binarySearch([1, 2, 3, 4, 5], 4)
#index = binarySearch([1, 2, 3, 4, 5], 8)
print(index)  