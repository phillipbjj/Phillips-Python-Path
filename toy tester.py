def characterFrequency(string):
    letterDict = {}
    organizedList = []

    # Count the frequency of each character in the string
    for letter in string:
        for single in letter:
            letterDict[single] = letterDict.get(single, 0) + 1

    # Use a simple sorting approach without sorted() or lambda
    items_list = list(letterDict.items())

    # Sort the items by count first
    items_list.sort(key=lambda x: -x[1])

    # Sort alphabetically for items with the same count
    for i in range(len(items_list) - 1):
        if items_list[i][1] == items_list[i + 1][1] and items_list[i][0] > items_list[i + 1][0]:
            items_list[i], items_list[i + 1] = items_list[i + 1], items_list[i]

    for key, value in items_list:
        organizedList.append((key, value))

    return organizedList

print(characterFrequency('mississippi'))
