#Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#Return any answer array that satisfies this condition.
#Input: nums = [4,2,5,7]     Output: [4,5,2,7]
 
def sortArrayByParity2(nums):
    even = 0
    odd = 1
    size = len(nums)
    while even < size and odd < size:
        if nums[even] % 2 == 0:
            even += 2
        elif nums[odd] % 2 == 1:
            odd += 2
        else:
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2
    return nums

nums = [4,2,5,7] 
print(sortArrayByParity2(nums))
