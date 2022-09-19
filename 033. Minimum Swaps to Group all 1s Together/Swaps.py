def minSwaps(nums):
    # Count the total number of 1s in the array
    totalOnes = nums.count(1)
        
    # Variable that will be returned at the end as minimum swap count
    minSwapsRequired = len(nums) + 1
        
    # If the number of 1s in the array is 0 that simply means 0 swaps needed as there is no 1 at all
    if totalOnes <= 1: return 0
        
    # Since the last element of array is adjacent to the first element (circular), just append this array to itself to take care of that property
    nums += nums
        
    i, j = 0,0
    zeros = 0
        
    # Sliding window approach begins
    while j < len(nums):
        # If current number is a zero, increment the count of zeros
        if nums[j] == 0: zeros += 1
            
        # We want to find a window of length = total Number of 1s.
        if j - i + 1 < totalOnes: j += 1
        # If window length is = total number of 1s, just check if the number of zeros in this window is less than previous window
        # Is yes, update the minSwapsRequired count
        else:
            # If this window has no zeros, it means no swaps needed so we can return from here
            if zeros == 0: return 0
            minSwapsRequired = min(minSwapsRequired, zeros)
            if nums[i] == 0: zeros -= 1
            i += 1
            j += 1
        
    return minSwapsRequired

nums = [0,1,1,1,0,0,1,1,0]
swaps = minSwaps(nums)

print("Minimum number of swaps required to group all 1s together ->", swaps)