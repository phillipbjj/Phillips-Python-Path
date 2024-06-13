"""You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

Example 1:
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3."""

def kthFactor(n, k):
    i = 1
    
    while i < n: 
        if n % i == 0: 
            if i == k:
                return i
        i += 1
        
    else:
        return -1        
    
    



n = 4
k = 4
print(kthFactor(n,k))