def findSubstring(s, words):
    output = []
        
        
    # Count the frequency of each word in words
    dict1 = {}  
    for word in words: dict1[word] = dict1.get(word,0) + 1     
        
    # Length of each word
    n = len(words[0])
        
    # Window Size = (length of words list * length of each word in the list)
    k = len(words) * n
        
    # Sliding Window Pointers
    i,j = 0,0
        
        
        
    while j < len(s):
        if j - i + 1 < k: j += 1
        else:
            # Here, we got a substring of length = k
            substring = s[i:j+1]
                
            # Now, create another map for this one and check all substrings of size = len(words[0])
            # Because we want this map to have same keys and same count as the map for words list
            dict2 = {}
            start = 0
            while start < len(substring):
                sub_substr = substring[start: start + n]
                dict2[sub_substr] = dict2.get(sub_substr, 0) + 1
                start += n
            # If both dictionaries are same, the append the starting index of this window to output
            if dict1 == dict2: output.append(i)

            i += 1
            j += 1
                

    return output


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print("Starting indices of all the concatenated substrings in s -> ", findSubstring(s,words))