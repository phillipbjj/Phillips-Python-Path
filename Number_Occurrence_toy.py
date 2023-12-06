
 #* Find the first item that occurs an even number of times in a list.
 #* Remember to handle multiple even-occurrence items and return the first one. 
 #* Return null if there are no even-occurrence items.
 #* example usage:
 #* onlyEven = evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4]);
 #* print(onlyEven); //  4


#def add_input_to_list(list_1):
#    item_1 = input("Give me the numbers: ")
#    list_1.append(item_1)
#    return list_1

#listOfNumbers = []
#add_input_to_list(listOfNumbers)
#print(listOfNumbers)


evenOccurrence = [1, 7, 2, 4, 5, 6, 8, 9, 6, 4]


findItem = 1
def occurrenceFinder(listFinder):
     for i in listFinder: #base case
         if listFinder[i] == listFinder[i + 1]:
             return listFinder[i]
         else:
             return occurrenceFinder(listFinder)
         
print(occurrenceFinder(evenOccurrence))
             
         
    


