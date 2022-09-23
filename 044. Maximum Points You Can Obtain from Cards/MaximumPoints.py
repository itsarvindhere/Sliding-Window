def maxScore(cardPoints, k):
    # Total Sum of the array
    totalSum = sum(cardPoints)
                       
    # If k is same as length of array, that means we need to take all the cards
    if k == len(cardPoints): return totalSum
        
    # To find the minimum sum of subarray of size = length - k
    minSum = totalSum
        
    #Sliding Window Pointers
    i,j = 0,0
        
    # Window Size
    windowSize = len(cardPoints) - k
        
    #Current Sum of window
    currSum = 0
            
    while j < len(cardPoints):
        currSum += cardPoints[j]
            
        if j - i + 1 < windowSize : j += 1
        else:
            minSum = min(minSum, currSum)
            currSum -= cardPoints[i]
            i += 1
            j += 1
            
    # Maximum sum of k cards = Total Sum of Array - minimum sum of left out cards
    return (totalSum - minSum)


cardPoints = [1,2,3,4,5,6,1]
k = 3

print("Maximum score we can obtain -> ", maxScore(cardPoints, k))