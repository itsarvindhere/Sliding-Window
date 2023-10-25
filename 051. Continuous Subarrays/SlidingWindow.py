from collections import deque


def continuousSubarrays(nums) -> int:
        
    # Subarray Count to return
    count = 0
        
    # Length of the list
    n = len(nums)
        
    # Deque for data about minimum elements
    minQ = deque()
        
    # Deque for data about maximum elements
    maxQ = deque()
        
    # Sliding window variables
    i,j = 0,0
        
    # Sliding window logic
    while j < n:
            
        # Remove all smaller elements from maxQ
        while maxQ and maxQ[-1] < nums[j]: maxQ.pop()
                
        # Remove all greater elements from minQ
        while minQ and minQ[-1] > nums[j]: minQ.pop()
                
        # Now, push current number's index in both the deques
        maxQ.append(nums[j])
        minQ.append(nums[j])
            
        # If the absolute difference between maximum and minimum in window [i,j] is not <= 2
        # Then, shrink the window from left side until the condition is true
        while minQ and maxQ and maxQ[0] - minQ[0] > 2: 
            if minQ[0] == nums[i]: minQ.popleft()
            if maxQ[0] == nums[i]: maxQ.popleft()
                    
            i += 1
            
        # At this point, the subarray from i to j is a continuous subarray
        # So, increment the count by the length of this subarray
        count += j - i + 1
            
        # And finally, slide the window from right side
        j += 1

    # Return the count
    return count

nums = [5,4,2,4]

print("Output -> ", continuousSubarrays(nums))