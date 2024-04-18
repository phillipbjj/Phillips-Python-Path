def countCharacters(words, chars):
    temp_chars = {}
    complete_words = {}
    for char in chars:
        temp_chars[char] = temp_chars.get(char, 0) + 1
        
    for word in words:
        check = True
        for letter in word:  
            if letter not in temp_chars:
                check = False
                break
        if check:
            complete_words[word] = complete_words.get(word, 0) + 1
    
    count = sum(len(key) for key in complete_words.keys())
    return count

words = ["cat","bt","hat","tree"]   
chars = "atach"

print(countCharacters(words, chars))