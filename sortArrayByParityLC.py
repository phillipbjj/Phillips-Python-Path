#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#Return any array that satisfies this condition.
#Input: nums = [3,1,2,4]    Output: [2,4,3,1]



def sortArrayByParity(nums):
    newArray = []
    
    for num in nums:
        if num % 2 == 0:
            newArray.insert(0, num)
        else:
            newArray.append(num)
            
    return newArray


nums = [3,1,2,4]
print(sortArrayByParity(nums))