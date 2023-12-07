evenOccurrence = [2, 3, 4, 5 ,6, 7, 4, 7, 2, 2, 2]
#evenOccurrence = [1, 3, 43, 5 ,6, 7, 4, 0, 8, 9, 2]
#evenOccurrence = [1, 7, 2, 7, 5, 6, 8, 9, 6, 7]
emptyList = []

def occurrenceFinder(evenList, i):
        if len(evenList) == 0:
            return print("Empty list")
        elif evenList.count(evenList[0]) == i:
            return emptyList.append(evenList[0]) #return evenList[0]
        #elif evenList.count(evenList[0]) != None:
            #return print("Null")
        else:
            return occurrenceFinder(evenList[1:], i)
         
print(occurrenceFinder(evenOccurrence, 2))

#need to add another list or a way to keep track of the numbers with 1 or more copies
#and get the value of the first