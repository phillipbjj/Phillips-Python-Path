def removeElement(nums, val):   
    k = len(nums)
    new_nums = []
    for num in nums:
        if num != val:
            new_nums.append(num)
    nums[:] = new_nums
            
    return k, new_nums
    
                                            




nums = [0,1,2,2,3,0,4,2]
val = 2