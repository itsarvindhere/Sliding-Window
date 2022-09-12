from collections import deque


def slidingWindowMaximum(nums,k):
    output = []
    maxQueue = deque()

    i,j = 0,0
    n = len(nums)

    while(j < n):
        #Calculations
        while(len(maxQueue) > 0 and nums[j] > maxQueue[-1]): maxQueue.pop()  
        maxQueue.append(nums[j])

        #Check Window size
        if(j - i + 1 < k): j += 1
        #If Window size = k
        else:
            #Put the maximum element in this window in the output
            output.append(maxQueue[0])
            #Calculations before sliding the window
            if(nums[i] == maxQueue[0]): maxQueue.popleft()
            #Slide the window
            i += 1
            j += 1

    return output


######################################
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print("Maximum in each Window of size k is ",  slidingWindowMaximum(nums,k))
######################################