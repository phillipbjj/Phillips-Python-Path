#You are given an array of strings words and a string pref.
#Return the number of strings in words that contain pref as a prefix.
#A prefix of a string s is any leading contiguous substring of s
#Input: words = ["pay","attention","practice","attend"], pref = "at"    Output: 2

#RUN TIME: 30MS     MEMORY: 11.80MB


def prefixCount(words, pref):
    prefix_dict = {}
    for word in words:
        if word[0:len(pref)] == pref:
            prefix_dict[word] = prefix_dict.get(word, 0) + 1
        else:
            continue
    
    
    answer = sum(prefix_dict.values())
    
    return answer
    
    
    
    
words = ["faeu","fauq","fanc","fap","favkigbbsk","faex","fag","faltrf","fabeckg","faem","fahh","nyyqmdv","faaei","fah","fayr","fazon","fairpv","fanz","fap","fanfxo","fadzmrtjv","famf","faom"]
pref = "fa"
#words = ["pay","attention","practice","attend"]    
#pref = "at"
print(prefixCount(words, pref))





"""fixlength = len(pref)
    prefix_dict = {}
    for word in words:
        if word[0:fixlength] == pref:
            prefix_dict[word] = prefix_dict.get(word, 0) + 1
        else:
            continue
    
    
    answer = len(list(prefix_dict))
    
    return answer"""