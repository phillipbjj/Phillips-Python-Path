
 #* Find the first item that occurs an even number of times in a list.
 #* Remember to handle multiple even-occurrence items and return the first one. 
 #* Return null if there are no even-occurrence items.
 #* example usage:
 #* onlyEven = evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4]);
 #* print(onlyEven); //  4


def occurrenceFinder(listFinder):
    secondList = []
    for i in listFinder: 
         listFinder.count(i)
         secondList.append(i)
         if listFinder.count(i) == secondList(i):
             return listFinder[i]
         else:
             return occurrenceFinder(listFinder[1:])
         
quit()         
def find_index(listIndex, value):
    if value < 0 or value >= len(listIndex):
        return None  
    return listIndex[value]
    

#evenOccurrence = [1, 7, 2, 4, 5, 6, 8, 9, 6, 4]
evenOccurrence = [2, 3, 4, 5 ,6, 7, 4, 7, 2, 2, 2]
#print(evenOccurrence.count(2))
#quit()
even_Value = occurrenceFinder(evenOccurrence)
print(occurrenceFinder(evenOccurrence))
print(find_index(evenOccurrence, even_Value))
         
    


