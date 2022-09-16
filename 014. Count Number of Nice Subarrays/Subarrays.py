# SOLUTION 1 - NOT O(1) SPACE
from collections import deque
def numberOfSubarraysSolution1(nums, k):
    subarrayCount = 0
        
    i,j = 0,0

    queue = deque()
        

    while( j < len(nums) ):
        # If we encounter an odd number push the index of this odd number to queue
        if(nums[j] % 2 != 0): queue.append(j)
            
        #If the number of odd numbers in this window exceeds k, then shrink the window from left until the count of odds is not greater than k
        if(len(queue) > k):
            while(len(queue) > k):
                #If the number at ith index is odd, that means we have to remove this odd number's index from queue
                if(nums[i] % 2 != 0): queue.popleft()
                #Shrink the window from left by incrementing i
                i += 1
            
        # If number of odd numbers in current window = k
        # Then total subarrays we can get out of this current window with k odd numbers => (leftmost odd number index - starting of window + 1)
        if(len(queue) == k): subarrayCount += queue[0] - i + 1
            
        #Increase window size from right side
        j += 1
            
        
    return subarrayCount

# SOLUTION 2 - O(1) SPACE
#This method finds number of subarrays with at most K odd numbers
def atMost(nums,k):
        
        countOfSubarrays = 0
        
        i,j = 0,0
        n = len(nums)
        
        countOfOdds = 0
        
        while j < n:
            if nums[j] % 2 != 0 : countOfOdds += 1
                
            if countOfOdds > k:
                while countOfOdds > k:
                    if nums[i] % 2 != 0: countOfOdds -= 1
                    i += 1
            
            countOfSubarrays += j - i + 1
            j += 1
        
        return countOfSubarrays
        
def numberOfSubarrays(nums, k):
        return atMost(nums, k) - atMost(nums, k-1)



nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

count = numberOfSubarraysSolution1(nums,k)

print("Number of Nice Subarrays -> ", count)