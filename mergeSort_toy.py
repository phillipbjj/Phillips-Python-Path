"""Given an array of N items, Merge Sort will:
Merge each pair of individual element (which is by default, sorted) into sorted arrays of 2 elements,
Merge each pair of sorted arrays of 2 elements into sorted arrays of 4 elements,
Repeat the process...,
Final step: Merge 2 sorted arrays of N/2 elements (for simplicity of this discussion, we assume that N is even) to obtain a fully sorted array of N elements.
This is just the general idea and we need a few more details before we can discuss the true form of Merge Sort."""


def merge_sort(list):

    if len(list) <= 1:
        return list

    leftSide_list, rightSide_list = split(list)
    left = merge_sort(leftSide_list)
    right = merge_sort(rightSide_list)

    return merge(left, right)

def split(list):

    """if left is None:
        left = 0
    if right is None:
        right = len(list) - 1
    mid = (left + right) // 2"""
    
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    
    return left, right

def merge(left, right):
    
    l = []
    a = 0
    z = 0
    
    while a < len(left) and z < len(right):
        if left[a] < right[z]:
            l.append(left[a])
            a += 1
        else: 
            l.append(right[z])
            z += 1        
    
    while a < len(left):
        l.append(left[a])
        a += 1
    while z < len(right):
        l.append(right[z])
        z += 1
        
    return l
print(merge_sort([8, 4, 5, 1, 3, 2, 6 ,7]))