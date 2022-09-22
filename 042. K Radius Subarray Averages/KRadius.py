def getAverages(nums, k):
    # Window Size = Diameter = 2 * radius
    # Since 0 indexed, so window size = (2 * radius) + 1
    windowSize = (2 * k) + 1
        
    #This is the output array we have to fill. Initialize each value with -1
    output = [-1] * len(nums)
        
    i,j = 0,0
    currSum = 0
        
    # General Fixed Size Sliding Window Template
    while j < len(nums):
        # Keep calculating the sum
        currSum += nums[j]
            
        # If the current window is not of size = windowSize, increment j
        if j - i + 1 < windowSize: j += 1
        # If window length = windowSize
        else:
            # Calculate the average
            avg = int(currSum/windowSize)
            # The center of this window is at i + k so set the value of i + k index as avg
            output[i + k] = avg
                
            # Remove Calculations for the ith index
            currSum -= nums[i]
                
            # Slide the window
            i += 1
            j += 1

    return output

nums = [7,4,3,9,1,8,5,2,6]
k = 3

print("K-radius averages -> ", getAverages(nums,k))