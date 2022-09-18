def maxFreq(s, maxLetters, minSize, maxSize):    
    # To keep track of uniques
    dict = {}
        
    # To store the valid substrings and number of times they appear
    substrings = {}
        
        
    i,j = 0,0

    while j < len(s):
            
        dict[s[j]] = dict.get(s[j],0) + 1
            
        # If window size is not yet minSize, increment j
        if (j - i + 1) < minSize: j += 1
        # If window size became minSize, now check the condition for unique letters
        else:
            if len(dict) <= maxLetters:
                substr = s[i:j+1]
                substrings[substr] = substrings.get(substr,0) + 1
                
            # Before sliding the window, remove the calculations for ith character
            dict[s[i]] -= 1
            if dict[s[i]] == 0: dict.pop(s[i])
            i += 1
            j += 1
        
    # If substrings dictionary is empty that means we did not find a valid substring as per the rules    
    # Otherwise, return the maximum count from the dictionary
    return 0 if not substrings else max(substrings.values())


s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4

freq = maxFreq(s, maxLetters, minSize, maxSize)

print("Maximum number of ocurrences of any substring follwing the rules ->", freq)