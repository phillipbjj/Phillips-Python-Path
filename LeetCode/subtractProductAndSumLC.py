#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15 """


def subtractProductAndSum(n):
    n = str(n)
    saved = 1
    saved2 = 0
    for number in n:
        number = int(number)
        saved *= number
        saved2 += number
    
    return (saved -saved2)
n = 234

print(subtractProductAndSum(n))