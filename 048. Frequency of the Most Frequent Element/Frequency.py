def maxFrequency(nums, k):
    maxFreq = 0
        
    # Sort the numbers first
    nums.sort()
        
    i,j = 0,0
    currSum = 0
    while j < len(nums):
        currSum += nums[j]
        # The largest number for any window at any time is the current/jth element
        # So we want to know how many moves will it take to make all elements of this window = j
        # If each element becomes j, that means total sum will be nums[j] * number of elements in window
        # And we want that to be either less than or equal to sum of this window + moves we have
        while nums[j] * (j - i + 1) > currSum + k: 
            currSum -= nums[i]
            i += 1
            
        # If we are here, that means, this is a valid window
        maxFreq = max(maxFreq, j - i + 1)
        j += 1
            
    return maxFreq


nums = [1,4,8,13]
k = 5


print("Maximum possible frequency of an element after performing at most k operations ->", maxFrequency(nums,k))