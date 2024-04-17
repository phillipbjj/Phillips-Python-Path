
def countCharacters(words, chars):
    temp_chars = {}
    complete_words = {}
    characterCount = 0
    for char in chars:
        for letter in char:
            temp_chars[letter] = temp_chars.get(letter, 0) + 1

    for word in words:
        for letter in word:
            if letter in temp_chars:
                complete_words[word] = complete_words.get(word, 0) + 1
            else: 
                break
        
    for word in words:
        if word in complete_words and len(word) == complete_words[word]:
            characterCount += complete_words[word]
            
    return characterCount

words = ["cat","bt","hat","tree"]   
chars = "atach"

print(countCharacters(words, chars))