#Write a short program that takes in an input number and returns it's factorial.
#For example, the factorial of 6 is
#6 x 5 x 4 x 3 x 2 x 1 = 720
#Note: The factorial of 0 is 1.
#ok... lets go! 

print("I heard wanna know the factorial my brotha!")
numba = input("Gimme a numba and I got you: ")
beef = int(numba)   
hehe_beef = beef
factorial_storage = []
while (beef != 0):
        if (beef == 0):
            print("The factorial of 0 is 1.")  
        elif (beef > 0):
            factorial_storage.append(beef)
            beef = (beef - 1) 
        elif (beef < 0):
            factorial_storage.append(beef)
            beef = (beef + 1) 
#print(factorial_storage)

factorial = 1 #factorial_storage[0] - can you explain this, i had to cheat and set to 1, I am having issues going through lists
for factory_slave in factorial_storage:
    factorial *= factory_slave 

print("Now! Let me show you the factorial of", hehe_beef)
print("BOOM! BIP BOP BOW!", factorial)


