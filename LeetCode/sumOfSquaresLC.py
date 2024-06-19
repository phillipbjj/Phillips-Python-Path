"""You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums."""



def sumOfSquares(nums):
    index = 0
    n = len(nums)
    sumSquares = 0
    while index <= n:
        if n % (index + 1) == 0:
            sumSquares += nums[index] ** 2
        index += 1
    return sumSquares


nums = [2,7,1,19,18,3] #63
#nums = [1, 2, 3, 4]
print(sumOfSquares(nums))