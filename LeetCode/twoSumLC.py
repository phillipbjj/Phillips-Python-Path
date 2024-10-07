#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
        numDict = {}
        for i, num in enumerate(nums):
            # Calculate the complement that would add up to the target
            complement = target - num
            # Check if the complement is already in the dictionary
            if complement in numDict:
                # If found, return the indices of the complement and the current number
                return [numDict[complement], i]
            # If not found, add the current number and its index to the dictionary
            numDict[num] = i
        
        
nums = [3,2,4]   
#nums = [2,7,11,15]
target = 9
twoSum(nums, target)