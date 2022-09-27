from collections import deque
def minKBitFlips(nums, k):
    flips = 0
    q = deque()
        
    for i,num in enumerate(nums):
        # Number of Items in queue = how many times current index has been flipped
        # So if 0 is flipped even times, it will be 0 again. That means, we need to flip it again
        # Similarly, if 1 is flipped odd times, it will be 0 again. So we need to again flip it to get 1 back
            
        condition1 = num == 0 and len(q) % 2 == 0
        condition2 = num == 1 and len(q) % 2 != 0
            
        # If any of the two conditions are true, that means we need to flip this k-length window
        # So put the last index of this window in queue to keep track of flips
        if condition1 or condition2: 
            flips += 1
            q.append(i + k - 1)
            
        # Remove the index from queue if we are done traversing the k-length window
        if q and i >= q[0]: q.popleft()
        
    return -1 if q else flips



nums = [0,0,0,1,0,1,1,0]
k = 3

print("Minimum number of k-bit flips required so that there is no 0 in the array -> ", minKBitFlips(nums,k))