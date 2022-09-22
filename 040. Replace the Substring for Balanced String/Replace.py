from collections import Counter
def balancedString(s):
    minLength = len(s)
        
    # Keep the count of each character in given string
    counter = Counter(s)
        
    n = int(len(s)/4)
            
    # What are extra characters and how many extra times they occur?
    extra = {}
    for c in counter: 
            if counter[c] > n: extra[c] = counter[c] - n
        
    # If no character occurs extra, that simply means string is already balanced
    if not extra: return 0
        
    # Number of distincts in extras
    distincts = len(extra)
        
    # Sliding Window Pointers
    i,j = 0,0
        
        
    # And now, the question becomes - Find the smallest substring with the extra characters
    while j < len(s):
        if s[j] in extra: 
            extra[s[j]] -= 1
            if extra [s[j]] == 0: distincts -= 1
            
        while distincts == 0:
            minLength = min(minLength, j - i + 1)
            if s[i] in extra:
                extra[s[i]] += 1
                if extra [s[i]] == 1: distincts += 1 
            i += 1
            
        j += 1       
        
    return minLength

s = "QQQW"

print("Minimum length of the substring that can be replaced with any other string of the same length to make s balanced -> ", balancedString(s))