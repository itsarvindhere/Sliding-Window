from collections import Counter
def checkInclusion(s1, s2):
        
    # Maintain the count of each character in string s1
    map = Counter(s1)
        
    # Number of distinct integers in s1 = length of the above counter
    distincts = len(map)
        
    i,j = 0,0
        
    # Size of Window/Substring in s2 = length of s1
    k = len(s1)
        
    while j < len(s2):
        # If current character is present in the map, decrement its count in map
        if s2[j] in map: 
            map[s2[j]] -= 1
            #If its count is 0, that means we can reduce one distict character
            if map[s2[j]] == 0: distincts -= 1
            
        # If window size is not yet k, increment j
        if j - i + 1 < k: j += 1
        #If window size is k
        else:
            # If the number of distincts are 0 that means current window has all the characters of string s1 in same frequency
            if distincts == 0: return True
                
            #Before incrementing i, check if ith character is there in map. If it is, then increment its count
            # This basically means we now need to find this character in next window since it is being removed from current window as we slide it
            if s2[i] in map:
                map[s2[i]] += 1
                # If count is back to 1, then distincts will also be incremented now as we now have one distinct character more to find
                if map[s2[i]] == 1: distincts += 1
                
            # Slide the window
            i += 1
            j += 1
            
        
    return False

s1 = "ab"
s2 = "eidbaooo"

hasPermutation = checkInclusion(s1,s2)

print("s1's permutation is present in s2  -> ", hasPermutation)