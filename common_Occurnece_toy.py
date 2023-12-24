
#Write a function `f(a, b)` which takes two strings as arguments and returns a
#string containing the characters found in both strings (without duplication), in the
#order that they appeared in `a`. 
#Remember to skip spaces and characters you have already encountered!
#Example: commonCharacters('acexivou', 'aegihobu')
#Returns: 'aeiou'
#Extra credit: Extend your function to handle more than two input strings.
#commonCharacters

apples = ["apepilou"]
bananas = ["aebinonu"]
kiwi = ["aeiou"]

#def commonCharacters(apples):
fruitBasket = {}
apples = ["apepilou"]
bananas = ["aebinonu"]
for fruit, fruit2 in apples, bananas:
        for juice, juice2 in fruit, fruit2:
	        fruitBasket[juice] = fruitBasket.get(juice, 0) + 1
	
print(fruitBasket)

#commonCharacters(apples)