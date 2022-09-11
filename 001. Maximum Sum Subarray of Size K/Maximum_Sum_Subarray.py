def maxSumSubarray(list,k):
    i,j = 0,0
    n = len(list)

    max_sum = 0
    sum = 0
    while j < n:
        sum += list[j]
        #If window size is not k yet, keep incrementing j
        if(j - i + 1 < k): j += 1
        #If window size is k, then do the calculations for max sum
        elif(j - i + 1 == k):
            max_sum = max(sum, max_sum)
            #Before sliding the window to right, Remove the first element of previous subarray from the sum
            sum = sum - list[i]
            #Slide the window to right
            i += 1
            j += 1

    return max_sum


list = [2,5,1,8,2,9,1]
k = 3

maxSum = maxSumSubarray(list,k)
print("Max Sum of Subarray of Size K is -> ", maxSum)