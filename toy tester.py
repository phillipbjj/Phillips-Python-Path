def characterFrequency(string):
    letterDict = {}
    for letter in string:
        letterDict[letter] = letterDict.get(letter, 0) + 1

    # Convert the dictionary to a list of tuples
    tupleList = [[k, v] for k, v in letterDict.items()]

    # Sort the list of tuples using selection sort
    for i in range(len(tupleList)):
        min_index = i
        for j in range(i+1, len(tupleList)):
            # Compare counts
            if tupleList[min_index][1] < tupleList[j][1]:
                min_index = j
            # If counts are equal, compare keys
            elif tupleList[min_index][1] == tupleList[j][1] and tupleList[min_index][0] > tupleList[j][0]:
                min_index = j
        tupleList[i], tupleList[min_index] = tupleList[min_index], tupleList[i]

    return tupleList

print(characterFrequency('mississippi'))
