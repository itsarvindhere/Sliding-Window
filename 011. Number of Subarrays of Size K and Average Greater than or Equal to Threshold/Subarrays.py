# Problem -> https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

def numOfSubarrays(arr, k, threshold) -> int:
    #Variable to keep track of count of subarrays that satisfy the condition
    count = 0
        
    # To avoid division every time we get a subarray of size K
    # Since we want total/k >= threshold
    # That means we want total >= (threshold * k)
    threshold *= k
        
    i,j = 0,0
        
    #To keep track of total of all elements in a subarray
    total = 0
        
    while( j < len(arr)):
        total += arr[j]
            
        #If window size is not yet k, increase the window size
        if(j - i + 1 < k): j += 1
        #If window size is k, check the condition
        else:                
            #If total is greater than or equal to threshold, then we can increment the count
            if(total >= threshold): count += 1
                    
            # Before sliding the window, remove the calculations we did for ith element
            total -= arr[i]
                
            # Slide the Window
            i += 1
            j += 1
    return count
    
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

count = numOfSubarrays(arr,k,threshold)

print("Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold -> ", count)