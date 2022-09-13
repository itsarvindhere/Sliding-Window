def largestSubarray(arr,k):
    maxLength = 0

    i,j = 0,0
    sum = 0

    while(j < len(arr)):
        sum += arr[j]

        # If sum becomes > k that means we have to shrink the window until the sum is no longer > k
        if(sum > k):
            while(sum > k):
                sum -= arr[i]
                i += 1
        
        # If sum is equal to k then store the maximum of two lengths (previous length and curent length)
        if(sum == k):  maxLength = max(maxLength, (j - i + 1))

        # Increase the window size
        j += 1

    return maxLength


arr = [1,2,3,7,5]
k = 12

maxLength = largestSubarray(arr,k)

print("Length of Largest Subarray with Sum K ->", maxLength)