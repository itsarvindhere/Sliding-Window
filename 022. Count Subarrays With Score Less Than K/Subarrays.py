def countSubarrays(nums, k):
        
    # To maintain the count the number of subarrays with score < k
    count = 0
    i,j = 0,0
    n = len(nums)
        
    #Keep track of sum of each window
    sum = 0
        
    while j < n:
        sum += nums[j]            
            
        # Length of a subarray/window => j - i + 1
        # So score = sum * length => sum * (j - i + 1)
        while sum * (j - i + 1) >= k:
            sum -= nums[i]
            i += 1
            
        # When we reach here, the curent subarray will have score < k only
        # And that means, the number of valid subarrays we can further get from this subarray = length of this subarray/window
        count += j - i + 1
        j += 1
            
    return count

nums = [2,1,4,3,5]
k = 10

count = countSubarrays(nums,k)

print("Number of Subarrays with Score strictly less than K ->", count)