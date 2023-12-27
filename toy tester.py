#math arranger toy time


mathProblems = ["50 + 50", "1007 + 1337", "123 + 321", "365 - 24"]
apples = ["apepilou"]
bananas = ["aebinonu"]
veggies = ["aveggieous"]
fruitBasket = {}
fruitCase = {}
wingTray = {}
commonLetters = []
def commonCharacters(apples, bananas):	

	for fruit in apples:
		for juice in fruit:
			fruitBasket[juice] = fruitBasket.get(juice, 0) + 1		
	for fruit2 in bananas:
		for juice2 in fruit2:
			fruitCase[juice2] = fruitCase.get(juice2, 0) + 1
	for vegetable in veggies:
		for worm in vegetable:
			wingTray[worm] = wingTray.get(worm, 0) + 1

	for key in fruitBasket:
		if key in fruitCase and wingTray:
			commonLetters.append(key)
		elif key in wingTray:
			commonLetters.append(key)
        else:
			continue
	
	bigDog = ["".join(commonLetters)]
	return bigDog

print(commonCharacters(apples, bananas))