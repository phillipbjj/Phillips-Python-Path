#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.


def singleNumber(nums):
    numTracker = {}
    for num in nums:
        numTracker[num] = numTracker.get(num, 0) + 1
        
    for key, value in numTracker.items():
        if value == 1:
            return key

"""Better solution: 
    def singleNumber(nums):
        result = 0
        for num in nums:
            result ^= num
        return result"""
nums = [2,2,1]

singleNumber(nums)