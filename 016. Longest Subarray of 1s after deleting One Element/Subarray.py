def longestSubarray(nums):
        maxLength = 0
        
        i,j = 0,0
        
        #To keep track of how many zeros are there in current window
        countOfZero = 0
        
        while(j < len(nums)):
            #If current number if a zero, increase the count of zeros
            if(nums[j] == 0): countOfZero += 1
            
            #If count of zero becomes more than 1, that means this cannot be a valid subarray/window
            # so to make it valid, make count <= 1 by shrinking the window from left
            if(countOfZero > 1):
                while(countOfZero > 1):
                    if(nums[i] == 0): countOfZero -= 1
                    i += 1
            
            # And after doing above, we are sure that this window has either no 0 or 1 0 so it is a possible solution
            maxLength = max(maxLength, j - i + 1)
            
            j += 1
            
        # Finally, we are asked to return the subarray without that one zero so we can simply do maxLength - 1
        return maxLength - 1


nums = [0,1,1,1,0,1,1,0,1]
size = longestSubarray(nums)

print("Length of Longest Subarray with only 1s after removing one element is ->", size)