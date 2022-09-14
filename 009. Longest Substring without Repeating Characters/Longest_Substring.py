#Solution 1 using a Set

def longestSubstring1(S):
    maxLength = 0
    uniques = set()

    i,j = 0,0
    n = len(S)

    while(j < n):
        #Character that we want to insert in set
        c = S[j]

        #If this character is already present in the set we cannot add it unless we remove the character present. So, we will shrink the window and also remove the ith character from set, until character we want to insert is no longer in the set      
        if c in uniques:
            while(c in uniques):
                uniques.discard(S[i])
                i += 1

        # We can now safely insert
        uniques.add(c)

        # The length of the substring will be same as length of set since set only contains uniques
        maxLength = max(maxLength, len(uniques))

        #Increase the size of window
        j += 1

    return maxLength

# Solution 2 using a Dictionary
def longestSubstring2(S):
    maxLength = 0
    dict = {}

    i,j = 0,0
    n = len(S)

    while(j < n):
        #Character that we want to insert in set
        c = S[j]

        #If this character is already present in the dictionary, increment its count otherwise put it as a new key with value 1
        dict[c] = 1 if not c in dict else dict[c] + 1

        # If the count of element we inserted in dictionary is more than 1, that means we are not fulfilling the condition to keep only unique elements. So, to ensure that the element inserted is unique in current window, we will start removing elements from the beginning of the window until the count of current character is not 1
        if dict[c] > 1:
                while(dict[c] > 1):
                    dict[S[i]] -= 1
                    i += 1

        # Now we can find the max length by finding max of the previous length and current length
        maxLength = max(maxLength, len(j - i + 1))

        #Increase the size of window
        j += 1

    return maxLength

S = "pwwkew"

maxLength = longestSubstring1(S)

print("Length of Longest Substring with no repeating Characters is ", maxLength)