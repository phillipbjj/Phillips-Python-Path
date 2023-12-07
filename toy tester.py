#TESTING
#evenOccurrence = [2, 3, 4, 5 ,6, 7, 4, 7, 2, 2, 2]
#evenOccurrence = [1, 3, 43, 5 ,6, 7, 4, 0, 8, 9, 2]
evenOccurrence = [1, 7, 2, 4, 5, 6, 8, 9, 6, 4]

def occurrenceFinder(evenOccurrence):
    for i in evenOccurrence: 
         evenOccurrence.count(i)
         if evenOccurrence.count(i) % 2 == 0:
             return i
        
if occurrenceFinder(evenOccurrence) == None:
    print("Null")
else:
    print(occurrenceFinder(evenOccurrence))    

