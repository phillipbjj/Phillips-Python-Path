#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#Given an integer n, return true if n is an ugly number.
#Ugly numbers [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
def isUgly(n):
    if n <= 0:
         return False

    while n % 2 == 0:
          n //= 2
    while n % 3 == 0:
         n //= 3
    while n % 5 == 0:
         n //= 5

    return n == 1
    





#n = 6
n = 1
#n = 14


print(isUgly(n))