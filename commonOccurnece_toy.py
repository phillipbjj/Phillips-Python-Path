#Write a function `f(a, b)` which takes two strings as arguments and returns a
#string containing the characters found in both strings (without duplication), in the
#order that they appeared in `a`. 
#Remember to skip spaces and characters you have already encountered!
#Example: commonCharacters('acexivou', 'aegihobu')
#Returns: 'aeiou'
#Extra credit: Extend your function to handle more than two input strings.
#commonCharacters

#apples = ["apepilou"]
#bananas = ["aebinonu"]
#kiwi = ["aeiou"]


apples = ["apepilou"]
bananas = ["aebinonu"]
fruitBasket = {}
fruitCase = {}
def commonCharacters(apples, bananas):	
	for fruit in apples:
		for juice in fruit:
			fruitBasket[juice] = fruitBasket.get(juice, 0) + 1		
	for fruit2 in bananas:
		for juice2 in fruit2:
			fruitCase[juice2] = fruitCase.get(juice2, 0) + 1
	for key in fruitBasket, fruitCase:
		if 
		

print(commonCharacters(apples, bananas))
print(fruitBasket)
print(fruitCase)

#commonCharacters(apples)