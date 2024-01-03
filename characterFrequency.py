#Write a function that takes in a string and returns an array of
#arrays as shown below sorted in descending order by frequency and then by
#ascending order by character.
#     :: Example ::
#characterFrequency('mississippi') ===
#[
# ['i', 4],
# ['s', 4],
# ['p', 2],
# ['m', 1]
#]
#def characterFrequency(string) {
#  return result;
#};
#organizedList = [[single, letterDict[single]] for single in letterDict]
 #i is index, key1/value1 are keys & values of current tuple
 #j is index, key2/value2 are keys & values of every other tuple

def characterFrequency(string):
    letterDict = {}
    for letter in string:
        for single in letter:
            letterDict[single] = letterDict.get(single, 0) + 1
            
    organizedList = [[key, value] for key, value in letterDict.items()]
     
    for a in range(len(organizedList)):
        min_index = a
        for b in range(a+1, len(organizedList)):          
            if organizedList[min_index][1] < organizedList[b][1]:
                min_index = b
            elif organizedList[min_index][1] == organizedList[b][1] and organizedList[min_index][0] > organizedList[b][0]:
                min_index = b
        organizedList[a], organizedList[min_index] = organizedList[min_index], organizedList[a]
                      
    return  organizedList

print(characterFrequency('mississippi'))

