evenOccurrence = [2, 3, 4, 5 ,6, 7, 4, 7, 2, 2, 2]
#evenOccurrence = [1, 3, 43, 5 ,6, 7, 4, 0, 8, 9, 2]
#evenOccurrence = [1, 7, 2, 7, 5, 6, 8, 9, 6, 7]
emptyList = []


def occurrenceFinder(evenList):
    emptyList = []
    for i, listNum in enumerate(evenList):
        #print(i, listNum)
        evenList.count(listNum)
        if evenList.count(listNum) == 2:
            return emptyList.append(listNum)#,  occurrenceFinder(evenList[1:])
        else: 
            return occurrenceFinder(evenList[1:])
print(occurrenceFinder(evenOccurrence))        
quit()
def occurrenceFinder(evenList):
    evenList = []
    emptyList = []
    for i in (evenList):
         evenOccurrence.count(i)
         if evenOccurrence.count(i) == evenOccurrence[i]:
             return evenOccurrence[i]
         else:
            return occurrenceFinder(evenOccurrence[1:])

quit()
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
#check if they appear more than once
#if they do, put them into another list
#compare their positions of those numbers within the first list