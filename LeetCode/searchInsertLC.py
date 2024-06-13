#Given a sorted array of distinct integers and a target value, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.
#Input: nums = [1,3,5,6], target = 5        Output: 2
 
 
 
 
 
 
 
 
def searchInsert(nums, target):
    position = 0
    for num in nums:
        if num < target:
            position += 1
            continue
        elif num > target:
            break
        elif num == target:
            position = position
            return position
        
    
    return position 



nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))