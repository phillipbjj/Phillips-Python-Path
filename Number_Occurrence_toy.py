
 #* Find the first item that occurs an even number of times in a list.
 #* Remember to handle multiple even-occurrence items and return the first one. 
 #* Return null if there are no even-occurrence items.
 #* example usage:
 #* onlyEven = evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4]);
 #* print(onlyEven); //  4


evenOccurrence = [2, 3, 5, 5 ,6, 7, 5, 7, 2, 2, 2]
#evenOccurrence = [1, 3, 43, 5 ,6, 7, 4, 0, 8, 9, 2]
#evenOccurrence = [1, 7, 2, 7, 5, 6, 8, 9, 6, 7]
def occurrenceFinder(evenList):
    evenDict = dict()
    for i in (evenList):
        evenDict[i] = evenDict.get(i, 0) + 1
        if evenDict[i] == evenDict.get(2):
            return i

print(occurrenceFinder(evenOccurrence))

quit()  
#elif 2 not in evenDict.values():
            #return print("Null")
        #print(i)
         #if evenList == evenList[0]:
             ##else:
            #return occurrenceFinder(evenList[1:]) 
#if occurrenceFinder(evenOccurrence) == None:
    #print("Null")
#else:
    #print(occurrenceFinder(evenOccurrence))
    #dictionary = dict()
		#keys = ['hehe', 'haha', 'suicidal']
		#for key in keys :
			#dictionary[key] = dictionary.get(key, 0) + 1
		#print(keys)
#if evenList == evenList[0]:
        #return evenList.count(i)
         #else:
            #return occurrenceFinder(evenList[1:])

#if evenOccurrence[i] < evenOccurrence[i] and evenOccurrence.count(i) == 2
#check if they appear more than once
#if they do, put them into another list
#compare their positions of those numbers within the first list