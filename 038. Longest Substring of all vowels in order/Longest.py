def longestBeautifulSubstring(word):
    maxLength = 0
        
    i,j = 0,1
        
    # To keep track of different characters (as distincts need to be 5 for a valid substring)
    distincts = 0
        
    while j < len(word):
        if word[i] == "a":
            # Only if a substring starts with "a" we can check if this is a valid substring
            distincts = 1
            while j < len(word) and ord(word[j-1]) <= ord(word[j]):
                # Check if the current character is different from previous
                # In that case, we got one more distinct character
                if ord(word[j-1]) < ord(word[j]): distincts += 1
                j += 1
            # Now, update maxLength if we got 5 distinct characters (since there are 5 vowels)
            if distincts == 5: maxLength = max(maxLength, j - i)                    
            
        # Move to the next substring
        i = j
        j += 1
            
    return maxLength

word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"

print("Length of Longest Substring Of All Vowels in Order ->", longestBeautifulSubstring(word))