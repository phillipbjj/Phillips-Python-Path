#Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#Return any answer array that satisfies this condition.
#Input: nums = [4,2,5,7]     Output: [4,5,2,7]
 


def sortArrayByParity2(nums):
    redirect = {}
    evenDict = {}
    oddDict = {}
    newNums = []
    
    for i in nums:
        redirect[i] = redirect.get(i)
       
    for i in redirect:
        if i % 2 == 0:
            newNums.append(i)
        else:
        
        
            
        
                
    return newNums


nums = [4,2,5,7] 
print(sortArrayByParity2(nums))
