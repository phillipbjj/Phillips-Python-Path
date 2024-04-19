#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Input: nums = [1,2,3,1]    Output: true

#Runtime: 470ms     Memory: 25.76mb

def containsDuplicate(nums):
    comparison = {}
    for num in nums:
        comparison[num] = comparison.get(num, 0) + 1
        if comparison[num] == 2:
            return True
        else:
            continue
    return False
    
    
    
    

nums = [0,4,5,0,3,6]
#nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
