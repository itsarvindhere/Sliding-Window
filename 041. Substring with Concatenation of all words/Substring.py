def findSubstring(s,words):
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
                
            # Now, just copy the dict1 into another dictionary that we will be modifying as we check each substring of size len(words[0])
            # Because we want this map to have same keys and same count as the map for words list
            dict2 = dict1.copy()
            start = 0
            while start < len(substring):
                sub_substr = substring[start: start + n]
                if sub_substr in dict2:
                    dict2[sub_substr] -= 1
                    if dict2[sub_substr] == 0: dict2.pop(sub_substr)
                start += n
                    
            # If dict2 is empty, that means this substring is valid
            if not dict2: output.append(i)

            i += 1
            j += 1
                

    return output


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print("Starting indices of all the concatenated substrings in s -> ", findSubstring(s,words))