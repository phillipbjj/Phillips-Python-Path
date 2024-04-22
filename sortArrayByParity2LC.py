#Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#Return any answer array that satisfies this condition.
#Input: nums = [4,2,5,7]     Output: [4,5,2,7]
 
"""for number in range(len(array)):
        for bubble in range(0, len(array) - number - 1):
                if array[bubble] > array[bubble + 1]:
                     array[bubble], array[bubble + 1] = array[bubble + 1], array[bubble]"""

def sortArrayByParity2(nums):
    evenDict = {}
    oddDict = {}
    newNums = []
    
    for index in range(len(nums)):
        for number in range(len(nums) - index - 1):
            
            
        
    """for i in nums:
        if i % 2 == 0:
            evenDict[i] = evenDict.get(i)
        else:
            oddDict[i] = oddDict.get(i)
    
    for i in evenDict:
        newNums.append(i)
    for i in oddDict:
            i = oddDict[i]"""
        
    
    return nums


nums = [4,2,5,7] 
print(sortArrayByParity2(nums))
