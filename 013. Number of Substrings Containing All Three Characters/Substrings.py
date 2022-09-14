def numberOfSubstrings(s):

    #The count of substrings that we want to return
    count = 0
        
    # A Dictionary that keeps the track of count of "a", "b" and "c"
    dict = {"a" : 0, "b" : 0, "c" : 0}
        
    i,j = 0,0
    n = len(s)
        
    while(j < n):
        #Put the jth character in dictionary
        dict[s[j]] += 1
                
        # While we have all three characters in the current window, 
        # find how many substrings we can form if we also include the rest of the characters outside of this window
        # Why so? Because if current substring is valid,
        # then that means other substrings are also valid that can be created if we include characters outside of this window
        while(dict["a"] > 0 and dict["b"] > 0 and dict["c"] > 0):
                
            count += n - j
                
            #Shrink the window from left
            dict[s[i]] -= 1  
            i += 1
        # Increase the window size from right
        j += 1
                    
    return count

s = "abcabc"
count = numberOfSubstrings(s)


print("Number of Substrings Containing All Three Characters are ->", count)