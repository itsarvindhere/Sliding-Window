# Problem -> https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

def countGoodSubstrings(s):
        
	#To keep track of count of good substrings
    count = 0
        
	#Dictionary to keep the count of each character in a substring
    dict = {}
		
	#This variable keeps track of how many unique characters are there in current substring
    uniques = 0
        
    i,j = 0,0
    n = len(s)

    while(j < n):
            
        c = s[j]
		#If jth character is not in dictionary, that means not only we can add it, but that also means it is currently a unique character in substring
        if not c in dict:
            dict[c] = 1
            uniques += 1
        else:
            dict[c] += 1
            
		#If window length is not yet 3, increment j
        if(j - i + 1 < 3): j += 1
		#If window size is 3 that means we found a substring of length 3
        else:
			#To check if it is a good substring, just check if number of unique characters is 3 or not
            if(uniques == 3): count += 1
                
			#Now, just before sliding the window to right, reduce the count of ith character from map
            dict[s[i]] -= 1
				
			#If count becomes 0, that means we also need to reduce count of uniques and remove this key from dictionary
            if(dict[s[i]] == 0): 
                dict.pop(s[i])
                uniques -= 1
                
			# Slide the window
            i += 1
            j += 1
                
    return count


s = "aababcabc"
count = countGoodSubstrings(s)

print("Number of Substrings of size 3 with Distinct Characters are ->", count)