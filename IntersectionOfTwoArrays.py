#Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#Constraints: 1 <= nums1.length, nums2.length <= 1000, 0 <= nums1[i], nums2[i] <= 1000
#Input: nums1 = [1,2,2,1], nums2 = [2,2]    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [2,2]                              Output: [4,9]

#add nums to dictionary
#compare nums in dictionaries
#




def intersect(nums1, nums2):
    nums_dict1 = {}
    nums_dict2 = {}
    intersection = []
    for num in nums1:
        nums_dict1[num] = nums_dict1.get(num, 0) + 1
    for num in nums2:
        nums_dict2[num] = nums_dict2.get(num, 0) + 1
    
    for num in nums_dict1:    
        if num in nums_dict2:
            if num not in intersection:
                intersection.append(num)
            elif nums_dict2[num] > 1:
                intersection.append(num)
            else:
                continue
            
    for num in nums_dict2:
        if num in nums_dict1:
            if num not in intersection:
                intersection.append(num)
            elif nums_dict1[num] > 1:
                intersection.append(num)
            else:
                continue
            
        
    return intersection
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
#nums1 = [1, 2, 2, 1]
#nums2 = [2,2]
print(intersect(nums1, nums2))