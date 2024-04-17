
def countCharacters(words, chars):
    temp_chars = {}
    complete_words = {}

    for char in chars:
        for letter in char:
            temp_chars[letter] = temp_chars.get(letter, 0) + 1

    for word in words:
        for letter in word:
            if letter in temp_chars:
                

        
    return temp_chars
   
    

words = ["cat","bt","hat","tree"]   
chars = "atach"

print(countCharacters(chars))