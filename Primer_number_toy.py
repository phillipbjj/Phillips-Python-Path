 #* A prime number is a whole number that has no other divisors other than
 #* itself and 1. Write a function that accepts a number and returns true if it's
 #* a prime number, false if it's not.
#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#However, this function does not correctly check if a number is prime. 
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Therefore, to check if a number x is prime, you should divide it by all numbers from 2 up to the square root of x. 
# If x is divisible by any of these numbers, then it is not prime. If x is not divisible by any of these numbers, then it is prime.
primes = list(range(1, 101))

x = 97
def primeNumberFunction(x):
    x_sqrt = x ** 0.5
    x_sqrt2 = int(x_sqrt)
    if x == 0:
        return "False"
    elif x == 2:
        return "True"
    
    for prime in range(2, (x-1)):
        if x != prime and x % prime == 0:
            return "False"
        elif x % x_sqrt2 == 0:
            return "False" 
        else:
            return "True"
        
#x_sqrt = x ** 0.5   
  
print(primeNumberFunction(x))