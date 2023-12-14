 #* A prime number is a whole number that has no other divisors other than
 #* itself and 1. Write a function that accepts a number and returns true if it's
 #* a prime number, false if it's not.
#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes = list(range(1, 101))

x = 7
def primeNumberFunction(x):
    for numba in range(2, 10):
        if x != numba and x % numba == 0:
            return "False"
        elif (x / x == 1) or (x / 1 == x):
            return "True"
    
    
print(primeNumberFunction(x))