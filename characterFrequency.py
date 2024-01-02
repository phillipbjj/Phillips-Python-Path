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
    organizedList = []
    for letter in string:
        for single in letter:
            letterDict[single] = letterDict.get(single, 0) + 1
    while True:
        organized = False
        for key1, value1 in letterDict.items():    
            for key2, value2 in letterDict.items():    
                if key1 == key2:
                    continue
                
                if value1 > value2 or (value1 == value2 and key1 < key2):
                        organizedList.append((key1, value1))
                        organized = True
                elif value1 < value2 or (value1 == value2 and key1 > key2):
                        organizedList.append((key2, value2))
                        organized = True
                   
        if not organized:
            break
                    
    return  organizedList

print(characterFrequency('mississippi'))

