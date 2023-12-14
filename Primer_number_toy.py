 #* A prime number is a whole number that has no other divisors other than
 #* itself and 1. Write a function that accepts a number and returns true if it's
 #* a prime number, false if it's not.
#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#However, this function does not correctly check if a number is prime. 
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Therefore, to check if a number x is prime, you should divide it by all numbers from 2 up to the square root of x. 
# If x is divisible by any of these numbers, then it is not prime. If x is not divisible by any of these numbers, then it is prime.
primes = list(range(1, 101))

x = 17
def primeNumberFunction(x):
    prime = 1
    for divisor in range(2, 10):
        if x != divisor and x % divisor == 0:
            return "False"
        elif (x / x == 1) or (x / 1 == x):
            return prime == x
        elif x / prime != 1:
            return "True"
    
    
print(primeNumberFunction(x))