def maxVowels(s,k):
        
        #Set of Vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        #This will keep track of maximum vowels in a k length substring
        maxCount = 0
        
        i,j = 0,0
        
        #This will keep track of count of vowels in a substring
        count = 0
        
        while( j < len(s)):
            #If current alphabet is a vowel, increment the count of vowels
            if(s[j] in vowels): count += 1
                
            # If the window size is not yet k, then increment j
            if(j - i + 1 < k): j += 1
            #If the window size becomes = = k, update maxCount if count > maxCount
            else:
                maxCount = max(maxCount, count)
                
                #Before sliding the window, remove the count for ith alphabet if it is a vowel
                if(s[i] in vowels): count -= 1
                    
                #Slide the window
                i += 1
                j += 1
            
        return maxCount

s = "abciiidef"
k = 3

maxCount = maxVowels(s,k)

print("Maximum Number of Vowels in any substring of length k are ->", maxCount)

