def maximumUniqueSubarray(nums):
        #Dictionary to keep track of each number and its count
        dict = {}
        
        i,j = 0,0
        n = len(nums)
        
        #To get the maximum score that we want to return
        maxSum = 0
        
        #To store the sum of current window
        sum = 0
        
        while(j < n):
            #Put the jth index element into dictionary
            dict[nums[j]] = 1 if not nums[j] in dict else dict[nums[j]] + 1
            # And also add it to sum
            sum += nums[j]
            
            # If the count is more than 1 that means this window cannot be a valid window of only unique numbers
            # Hence, we have to shrink this window until the count for number at jth index is no longer more than 1
            if(dict[nums[j]] > 1):
                while(dict[nums[j]] > 1):
                    dict[nums[i]] -= 1
                    #When we shrink, we also need to make sure we are reducing the item that we remove from the beginning of this window, from the sum
                    sum -= nums[i]
                    i += 1
            #If we are here, that means we have a valid subarray as per the condition given so we can update our maxSum if the sum of current subarray is greater
            maxSum = max(maxSum, sum)
            j += 1
            
        return maxSum


nums = [5,2,1,2,5,2,1,2,5]

maxScore = maximumUniqueSubarray(nums)

print("Maximum score we can get ->", maxScore)