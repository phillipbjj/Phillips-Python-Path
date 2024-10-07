#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".



def longestCommonPrefix(strs):
    if not strs:
        return ""
    # Start with the first string in the array as the prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Reduce the prefix length until it matches the start of the string
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
    
    
    
strs = ["flower", "flow", "flight"]
longestCommonPrefix(strs)
#Output: "fl"
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.