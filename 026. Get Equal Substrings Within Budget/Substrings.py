def equalSubstring(s, t, maxCost):
    # To keep track of maximum substring length that satisfied the condition
    maxLength = 0
        
    i,j = 0,0
    cost = 0
        
    while j < len(s):
        # Find the cost of replacement if we include a character in this window
        cost += abs(ord(s[j]) - ord(t[j]))
            
        # If adding the character violates the condition, shrink the window from beginning till condition is satisfied
        while cost > maxCost:
            cost -= abs(ord(s[i]) - ord(t[i]))
            i += 1
            
        # And now just update the maxlength if length of current window is bigger than previous maxLength
        maxLength = max(maxLength, j-i+1)
        j += 1
        
        return maxLength


s = "abcd"
t = "cdef"
maxCost = 3

length = equalSubstring(s,t,maxCost)

print("Maximum Length of Substring ->", length)