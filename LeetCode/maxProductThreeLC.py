#Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""Example 1:

Input: nums = [1,2,3]
Output: 6
Constraints:

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000
"""
def maximumProduct(nums):
    products = []
    maxProd = 0
    prod = 1
    i = 0
    for num in nums:
        prod *= num
        print(prod)
        products.append(prod)
        
        
    
    
    
    
    
    
    return None


nums = [-1,2,-3,4] #Outcomes: 

print(maximumProduct(nums))