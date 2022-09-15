def minSubArrayLen(target, nums):
        
        #Initialize length with infinity
        maxValue = float('inf')
        length = maxValue
                
        i,j = 0,0
        
        sum = 0
        
        while( j < len(nums)):
            sum += nums[j]
            
			#If sum so far is >= target, find what is the smallest length of subarray we can get from this window which fulfills the condition
            if(sum >= target):
                while(sum >= target):
                    length = min(length, j - i + 1)
					#Shrink the window from left side
                    sum -= nums[i]
                    i += 1
			#Increase the window size from right side
            j += 1
            
            # If length is still infinity, that means we did not get any subarray that fulfills this condition so in that case we can return 0
        return 0 if length == maxValue else length

target = 7
nums = [2,3,1,2,4,3]

minimumLength = minSubArrayLen(target,nums)

print("Length of Smallest Subarray is -> ", minimumLength)

