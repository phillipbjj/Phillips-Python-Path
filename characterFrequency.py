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


def characterFrequency(string):
    letterDict = {}
    for letter in string:
        for single in letter:
            letterDict[single] = letterDict.get(single, 0) + 1
    for a, (key1, value1) in letterDict.items():    #i is index, key1/value1 are keys & values of current tuple
        for b, (key2, value2) in letterDict.items():    #j is index, key2/value2 are keys & values of every other tuple
            if a == b:
                continue
            

   

        
    #organizedList = [[single, letterDict[single]] for single in letterDict]

    

    
    return letterDict.items() #organizedList[] 


print(characterFrequency('mississippi'))
