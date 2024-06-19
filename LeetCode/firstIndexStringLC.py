#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack, needle):
    
    if needle in haystack:
        return haystack.find(needle)
    """for string in range(0, len(haystack), len(needle)):
        if string == needle:
            return haystack[string]"""
    return -1
    
    



#haystack = "leetcode"
#needle = "leeto"
haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))