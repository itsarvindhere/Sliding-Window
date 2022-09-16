 #Method to find what is the maximum length subarray with at most K number of "T" or "F (based on what character we pass as argument)"
def maxConsecutive(answerKey,k,character):
        
    i,j = 0,0
    n = len(answerKey)
    count = 0
    maxCount = 0
        
    while j < n:
        c = answerKey[j]
        if c == character: count += 1
            
        while(count > k):
            if answerKey[i] == character: count -= 1
            i += 1
            
        maxCount = max(maxCount,j - i + 1) 
        j += 1
    return maxCount

def maxConsecutiveAnswers(answerKey, k):
    return max(maxConsecutive(answerKey,k, "F"), maxConsecutive(answerKey,k,"T"))


answerKey = "TTFTTFTT"
k = 1

maximum = maxConsecutiveAnswers(answerKey,k)

print("Maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times ->", maximum)