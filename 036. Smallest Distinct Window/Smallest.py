def findSubString(str):
    # Dictionary to keep track of each character in given string
    dict = {}

    # Initially, each character count is 0
    for s in str: 
        if not s in dict: dict[s] = 0

    # Initially, distincts = number of keys in dictionary
    distincts = len(dict)
        
    i,j = 0,0
    
    # To keep track of the smallest valid window
    minLength = len(str) + 1
        
    while j < len(str):
        # Increment the count in dictionary
        dict[str[j]] += 1
        #If count becomes 1 that means this character occurs at least once so distincts can be decremented by 1

        # Because we now have one less character to find
        if dict[str[j]] == 1: distincts -= 1
        
        # While the window is valid, what is the smallest window we can get out of it
        while distincts == 0:
            minLength = min(minLength, j - i + 1)
            dict[str[i]] -= 1
            if dict[str[i]] == 0: distincts += 1
            i += 1
            
        j += 1
        
                
    return minLength

str = "AABBBCBBAC"
smallest = findSubString(str)

print("Smallest Valid Substring Length is ->", smallest)