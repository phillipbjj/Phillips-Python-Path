#Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""Example 1:

Input: nums = [1,2,3]
Output: 6
Constraints:

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000
"""
def maximumProduct(nums):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    
    for num in nums:
        # Update the three largest numbers
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num
        
        # Update the two smallest numbers
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    return max(max1 * max2 * max3, min1 * min2 * max1)
nums = [-1,2,5,4] #Outcomes: 

print(maximumProduct(nums))