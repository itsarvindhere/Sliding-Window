def firstNegative(arr, k):
    output = []

    i,j = 0,0
    n = len(arr)

    negatives = []
    while(j < n):
        #Store the negatives in a list
        if(arr[j] < 0 ): negatives.append(arr[j])
        # If window is not of size k yet, increment j
        if(j - i + 1 < k): j += 1
        #If window is of size k, then get the solution for that window
        else:
            #Put the first negative number (or zero) in the output for current window
            output.append(0 if len(negatives) == 0 else negatives[0])

            if(arr[i] < 0): negatives = negatives[1:]
            i += 1
            j += 1

    return output


#Input
arr =  [-8, 2, 3, -6, -10]
k = 2

#Output
output = firstNegative(arr,k)
print("First Negative Number in each Window of Size K -> ", output)