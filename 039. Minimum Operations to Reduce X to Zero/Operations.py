def minOperations(nums, x):
    # Min Operations = Min number of elements to remove
    # Min number of elements to remove = length of list - maximum number of elements that aren't removed
    # This means, we can simply find maximum number of elements that aren't removed and then at the end substract it from length of list
    # If elements we remove had sum == x that means elements that we did not remove have sum => sum of whole list - x
  
    maxLength = -1
        
    totalSum = sum(nums)
    n = len(nums)
        
    i,j = 0,0
    sumSoFar = 0
        
        
    # Now think of what is the condition for a subarray to be a valid subarray of elements that are not removed?
        
    # If we remove the elements whose sum == x, that means the elements that are left have sum = (sum of whole list - x)
    # So, for any subarray to be a valid subarray of elements that are not removed, the sum of its elements needs to be (sum of list - x)
        
    while j < n:
        sumSoFar += nums[j]
            
        while i <= j and sumSoFar > totalSum-x:
            sumSoFar -= nums[i]
            i += 1
            
        if sumSoFar == totalSum-x: maxLength = max(maxLength, j - i + 1)
        j += 1
        
        
    return -1 if maxLength == -1 else n - maxLength


nums = [1,1,4,2,3]
x = 5

print("Minimum number of operations to reduce x to exactly 0 -> ", minOperations(nums,x))