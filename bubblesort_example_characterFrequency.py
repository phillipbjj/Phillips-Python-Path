#BUBBLE SORT OF CHARACTER FREQUENCY




def characterFrequency(string):
    letterDict = {}
    for letter in string:
        letterDict[letter] = letterDict.get(letter, 0) + 1

    # Convert the dictionary to a list of tuples
    freqList = list(letterDict.items())

    # Perform a bubble sort on the list
    for i in range(len(freqList)):
        for j in range(len(freqList) - i - 1):
            if freqList[j][1] < freqList[j + 1][1] or (freqList[j][1] == freqList[j + 1][1] and freqList[j][0] > freqList[j + 1][0]):
                freqList[j], freqList[j + 1] = freqList[j + 1], freqList[j]

    return freqList
