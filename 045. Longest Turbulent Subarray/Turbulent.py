# Helper method to check if current index can be included in window or not
def isTurbulent(arr, j):
    # If current element is greater than previous, then it should be greater than next as well
    condition1 = arr[j] > arr[j-1] and arr[j] > arr[j + 1]
            
    # If current element is smaller than previous, then it should be smaller than next as well
    condition2 = arr[j] < arr[j-1] and arr[j] < arr[j + 1]
        
    # If either of two statements are true, that means we can include index j in the window
    return condition1 or condition2
    
def maxTurbulenceSize(arr):
    n = len(arr)
    if n == 1: return 1

    maxSize = 1
        
    i,j = 0,1
        
    # General Sliding Window Template
    while j < n:
            
        # If previous and current values are same, we need to skip this window so increment starting pointer
        if arr[j-1] == arr[j]: i += 1
            
        # While this condition is true, we can expand the window
        while j + 1 < n and isTurbulent(arr,j): j += 1
                
        # As soon as above loop ends, we can update the maxSize if current window size is bigger than previous maxSize
        maxSize = max(maxSize, j - i + 1)
            
        i = j
        j += 1
        
    return maxSize



arr = [9,4,2,10,7,8,8,1,9]

print("Size of Longest turbulent Subarray is -> ", maxTurbulenceSize(arr))