
 #* Find the first item that occurs an even number of times in a list.
 #* Remember to handle multiple even-occurrence items and return the first one. 
 #* Return null if there are no even-occurrence items.
 #* example usage:
 #* onlyEven = evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4]);
 #* print(onlyEven); //  4


#evenOccurrence = [2, 3, 4, 5 ,6, 7, 4, 7, 2, 2, 2]
#evenOccurrence = [1, 3, 43, 5 ,6, 7, 4, 0, 8, 9, 2]
evenOccurrence = [1, 7, 2, 7, 5, 6, 8, 9, 6, 7]

def occurrenceFinder(evenOccurrence):
    for i in evenOccurrence: 
         evenOccurrence.count(i)
         if evenOccurrence.count(i) == evenOccurrence[0]:
             return evenOccurrence[i]
         else:
            return occurrenceFinder(evenOccurrence[1:])
        
if occurrenceFinder(evenOccurrence) == None:
    print("Null")
else:
    print(occurrenceFinder(evenOccurrence))
    


