# PROBLEM - https://leetcode.com/problems/max-consecutive-ones-iii/

def longestOnes(nums, k):
    # Maximum consecutive 1s just means the length of longest subarray
    maxLength = 0
        
    i,j = 0,0
    n = len(nums)
        
        
    # The condition is we can flip k 0s in the subarray. In other words, just find every subarray with at most k zeros and check its length
    # and then return the maximum length
    zeros = 0
        
    while(j < n):
        if(nums[j] == 0): zeros += 1
                
        # If number of zeros becomes more than k we need to shrink the window from left by incrementing i
        if(zeros > k):
            while(zeros > k):
                if(nums[i] == 0): zeros -= 1
                i += 1
            
        # Otherwise, this is a valid subarray so we can check if its length > previous maxLength
        maxLength = max(maxLength, j - i + 1)
            
        # Increase the window size from right by incrementing j
        j += 1
            
    return maxLength



nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

maxLength = longestOnes(nums,k)

print("Length of Longest Subarray with at most K zeros -> ", maxLength)