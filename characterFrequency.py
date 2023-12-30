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
            return  letterDict


print(characterFrequency('mississippi'))