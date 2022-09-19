def characterReplacement(s,k):
    # The Longest Substring length to return
    maxLength = 0
        
    # Dictionary to keep the track of how many times a character occurs in a substring
    dict = {}
    i,j = 0,0
        
    while j < len(s):
        dict[s[j]] = dict.get(s[j], 0) + 1
            
        # While this condition is true, shrink the window until (j - i + 1) - max(dict.values()) is no longer > k
        while (j - i + 1) - max(dict.values()) > k:
            dict[s[i]] -= 1
            i += 1
            
        # If we are here, that means (j - i + 1) - max(dict.values()) <= k so this window is a valid window that we can consider
        maxLength = max(maxLength, j - i + 1)
        j += 1
                        
    return maxLength


s = "AABABBA"
k = 1

longest = characterReplacement(s,k)

print("Length of the longest substring containing the same letters after atmost k replacements -> ", longest)