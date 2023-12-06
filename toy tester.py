#TESTING
evenOccurrence = [2, 3, 4, 5 ,6, 7, 4, 7, 2, 2, 2]
testList = []

def occurrenceFinder(evenOccurrence):
    for i in evenOccurrence: 
         evenOccurrence.count(i)
         testList.append(i)
         if evenOccurrence.count(i) == testList(i):
             return testList[i]
         else:
             return occurrenceFinder(evenOccurrence[1:])
        
        
def find_index(listIndex, value):
    if value < 0 or value >= len(listIndex):
        return None  
    return listIndex[value]
    

#even_Value = occurrenceFinder(evenOccurrence, testList)
print(occurrenceFinder(evenOccurrence))
#print(find_index(evenOccurrence, even_Value))
