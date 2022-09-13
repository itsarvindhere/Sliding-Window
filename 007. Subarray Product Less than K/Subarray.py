def numSubarrayProductLessThanK(nums, k):

    #If k is 0 or 1, there is no way we can have product less than 0 or 1 in any subarray
    if k <= 1: return 0
        
    count = 0
        
    i,j = 0,0
    product = 1
        
    while j < len(nums):
        # Multiply current number with current product
        product *= nums[j]
            
        #If the product we got is >k or =k, then in both cases, we want to shrink the window
        if product >= k:
            while(product >= k):
                product = int(product/nums[i])
                i += 1
            
        #After above check, we are sure that this particular window has product < k only.
        # This means, each element of the window also is a valid subarray in itself
        # In short, the length of this window is what we want to add to count
        count += j - i + 1
            
        #Increase the size of window
        j += 1
            
    return count


nums = [10,5,2,6]
k = 100
count = numSubarrayProductLessThanK(nums,k)

print("Number of Subarrays with Product of Elements less than K ->", count)