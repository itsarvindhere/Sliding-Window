#This method finds how many subarrays have sum <= goal
def subArraysWithAtMostGoalSum(nums,goal):    
        #If sum is negative, there can be no possible subarray since we have either 0 or 1
        if goal < 0: return 0
            
        count = 0
        sum = 0

        i,j = 0,0
        n = len(nums)

        while j < n:
            sum += nums[j]

            while(sum > goal):
                sum -= nums[i]
                i += 1
                
            count += j - i + 1
            j += 1
            
        return count
    
def numSubarraysWithSum(nums, goal):
        # Number of subarrays with sum exactly goal = (Number of subarrays with sum <= goal) - (Number of subarrays with sum <= goal - 1)
        return subArraysWithAtMostGoalSum(nums,goal) - subArraysWithAtMostGoalSum(nums, goal - 1)


nums = [1,0,1,0,1]
goal = 2

count = numSubarraysWithSum(nums,goal)

print("Number of non-empty subarrays with a sum  == goal ->", count)