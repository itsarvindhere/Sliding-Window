from collections import Counter
def minWindow(s, t):
        
    # If "t" string is longer than "s", we can never find a substring in "s"
    if len(t) > len(s): return ""
        
    # Initialize minLength with a bigger value
    minLength = len(s) + 1
        
    # Count of each character in the string "t"
    count = Counter(t)
        
    # Number of distinct characters in "t"
    distincts = len(count)
        
    # Pointers for the sliding window
    i,j = 0,0
        
    # Keep the starting and ending index of the smallest window
    minI = -1
    minJ = -1
        
        
    while j < len(s):
        if s[j] in count:
            count[s[j]] -= 1
            if count[s[j]] == 0: distincts -= 1
            
        # If current window is a valid substring, then check what can be the minimum valid substring out of this window
        # For that we can keep shrinking the window from left until the condition is no longer true
        while distincts == 0:
            # If current window has a smaller length than previous valid window, then consider this window as new possible solution
            if j - i + 1 < minLength:
                minLength = j - i + 1
                minI = i
                minJ = j
            if s[i] in count: 
                count[s[i]] += 1
                if count[s[i]] == 1 : distincts += 1 
            i += 1
            
        # Increase window size from right side
        j += 1 
        
    # Now that we got the starting and ending index of smallest window, just get the substring out of these
    substring = s[minI:minJ + 1]
        
    return substring

s = "ADOBECODEBANC"
t = "ABC"

smallestSubstring = minWindow(s,t)

print("Minimum Window Substring is ->", smallestSubstring)