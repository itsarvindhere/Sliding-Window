from collections import deque
def longestSubarray(nums, limit):
    maxLength = 0

    minQueue = deque()
    maxQueue = deque()
        
        
    i,j = 0,0
    n = len(nums)
        
    while j < n:
        # We only want bigger elements in maxQueue
        while len(maxQueue) > 0 and maxQueue[-1] < nums[j]: maxQueue.pop()
        maxQueue.append(nums[j])
            
        # We only want smaller elements in minQueue
        while len(minQueue) > 0 and minQueue[-1] > nums[j]: minQueue.pop()
        minQueue.append(nums[j])
            
        # Make sure the maximum absolute difference is <= limit
        while len(maxQueue) > 0 and len(minQueue) > 0 and maxQueue[0] - minQueue[0] > limit:
            if maxQueue[0] == nums[i]: maxQueue.popleft()
            if minQueue[0] == nums[i]: minQueue.popleft()
            i += 1
                
        # Update the maxLength if current window length is bigger than previous maxLength
        maxLength = max(maxLength, j - i + 1)
        j += 1
        
    return maxLength

nums = [8,2,4,7]
limit = 4

longestLength = longestSubarray(nums, limit)

print("Length of Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit -> ", longestLength)