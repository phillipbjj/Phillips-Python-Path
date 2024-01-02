def characterFrequency(string):
    letterDict = {}
    
    for letter in string:
        for single in letter:
            letterDict[single] = letterDict.get(single, 0) + 1
            
    return  letterDict


print(characterFrequency('mississippi'))