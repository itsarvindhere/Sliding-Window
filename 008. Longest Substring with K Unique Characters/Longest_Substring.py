def longestSubstring(S, K):
    maxLength = -1

    dict = {}

    i,j = 0,0
    n = len(S)

    while(j < n):
        c = S[j]
        dict[c] = 1 if not c in dict else dict[c] + 1

        # If number of unique characters becomes more than K we have to shrink the window till they are not more than K
        # To shrink the window size, we increment i but before doing that we also remove all the calculations for ith character
        if len(dict) > K:
            while(len(dict) > K):
                dict[S[i]] -= 1
                if(dict[S[i]] == 0): dict.pop(S[i])
                i += 1
        
        # If number of unique characters are same as K, we can save this length of window if it is more than current max
        if len(dict) == K: 
            maxLength = max(maxLength, j - i + 1)

        #Increase the size of the window
        j += 1

    return maxLength


S = "aabacbebebe"
K = 3

maxLength = longestSubstring(S,K)

print("Length of Longest Substring with K unique Characters is ", maxLength)