from collections import Counter
def countOccurances(txt, pat):
    anagrams = 0
    #Maintain a map of count of each character in pat
    map = Counter(pat)

    #How many distinct characters are in pat
    distincts = len(map)

    i,j = 0,0

    #Window Size
    k = len(pat)

    while(j < len(txt)):
        # If current character is present in the map, decrement its count in map
        if txt[j] in map:
            map[txt[j]] -= 1
            #If its count is 0, that means we can reduce one distict character
            if(map[txt[j]] == 0): distincts -= 1
        if(j - i + 1 < k): j += 1
        else:
            #If number of distinct characters is 0 that means current window has all the required characters in required frequency so it is an anagram
            if(distincts == 0): anagrams += 1

            #Before incrementing i, check if ith character is there in map. If it is, then increment its count
            if txt[i] in map: 
                map[txt[i]] += 1
                #And if the count is == 1 then increment distincts
                if(map[txt[i]] == 1): distincts += 1
            #Slide the window to right
            i += 1
            j += 1

    return anagrams


txt = "aabaabaa"
pat = "aaba"

print(countOccurances(txt,pat))