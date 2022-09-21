def longestContinuousSubstring(s):
    # The smallest continuous substring can be just one character
    longest = 1
        
    i,j = 0,1

    while j < len(s):
            
        # While j does not go out of bounds and current character is one more than previous
        # Keep incrementing j i.e., keep increasing window size from right side
        while j < len(s) and ord(s[j]) == ord(s[j-1]) + 1: j += 1
                
        # And now just update the length if current window's length is bigger than previous maxLength
        longest = max(longest, j - i)
            
        # And now we can update the pointers to move the window to find next valid substring
        i = j
        j += 1

    return longest

s = "abacaba"

print(" Length of the Longest Alphabetical Continuous Substring -> ", longestContinuousSubstring(s))