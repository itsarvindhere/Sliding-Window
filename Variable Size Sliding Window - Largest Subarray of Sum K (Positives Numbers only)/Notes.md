# PROBLEM STATEMENT

Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.


e.g. arr = [4,1,1,1,2,3,5], k = 5

This means, we need to find the length of longest sub-array with sum = 5 in above array.

Here are all the subarrays of sum = 5

    [4,1] -> Length is 2
    [1,1,1,2] -> Length is 4 <- Longest
    [2,3] - Length is 2
    [5] -> Length is 5

So, the longest sub-array length is 4. Hence, return 4.

# WHAT IS VARIABLE SIZED SLIDING WINDOW

In earlier problems, we had fixed sized sliding window. It means we were given the size already and we had to look at all the windows of that size only.

But in case of Variable Sized Sliding Window problems, we are not given the size. In fact, we have to find the size of the window based on the condition given in the problem statement. 

e.g., in above problem, size is not given but the condition is that the sum should be 5. So, we have to go through all the windows that sum to 5 and then see which window length is the maximum. That length will be the output.

# IDENTIFICATION OF VARIABLE SIZED SLIDING WINDOW

-> We will be given a problem related to Array or String
-> The problem will mention Subarray or Substring
-> We will be given the condition, K
-> And we will be asked to maximize or minimize the window size


# VARIABLE SIZED SLIDING WINDOW APPROACH

arr = [4,1,1,1,2,3,5], k = 5

We start i = 0, j = 0 just like in case of fixed size window.

Now, here, our objective is not to get to some specific window size. Instead, our objective is to get a sum = 5 in this window. 

Currently, j = 0. So at j index we have 4. 
Since sum right now is 0 and 0 < 5 that means we can add jth value to increase the sum
Sum = 4

Is sum == 5? NO! Which means we can increase the size of the window to find a possible candidate to be the output.

So, we increment j by 1. Now, j = 1 and at j index we have 1. 

Sum = 4 + 1 => 5

Is sum = 5? YES! This means, we got our first window with sum = 5. 

And the length of this window is 2 i..e, (j - i + 1) => (1-0 + 1) => 2

Since this window has sum = k, that means we can increase the size of our window. So, that means we can increment j.

This is important. In case of fixed sized window, we used to increment both i and j because the window size was fixed. But here, our window may increase in size or shrink. So, when its size has to increase, then we have to increment j and when its size has to shrink, then we increment i.

i = 0, j = 2. 

    sum = sum + 1 => 5 + 1 => 6

Because now sum became > k, that means we have to shrink the window. But how much we have to shrink?

Well, we have to shrink till the sum is no longer > k. i.e., it can be <= k but not > k.

So, while (sum > k) : shrink the window

How do we shrink? We increment i index and before incrementing remove the ith element from sum.

So, we increment i to i + 1 => 0 + 1 => 1

Since at 0th index we had 4 so we will remove 4 from the sum.

Sum = 6 - 4 => 2

Now, our sum is < k.  This means, we have to incrase the window size. So, we have to increment j this time. 

j = j + 1 => 2 + 1 => 3

At j = 3, we have 1 so add it to sum. Sum = 2 + 1 => 3

Now again, sum  < k which means we can increase the window size again so increment j.

j = j + 1 => 3 + 1 => 4

At j = 4, we have 2 so add it to sum. Sum = 3 + 2 => 5

And now, since sum == k, that means we found yet another window with sum 5. And the length of this window is (j - i + 1) => (4 - 1 + 1) => 4

Because this new length = 4 is greater than previous maxLength = 2, that means we can update maxLength = 4

And as we found a solution, we move on to find next solution by increasing window size. i.e., j += 1

j = j + 1 => 4 + 1 => 5

At j = 5, we have 3 so add it to sum. Sum = 5 + 3 => 8

Now again, our sum became > k which means once again, we have to reduce the sum till it is <= k i.e., we have to shrink the window.

So, while(sum > k): shrink the window

At i = 1 index currently we have 1. So, we do sum = sum - arr[i] => 7
and i = i + 1 => 2

At i = 2 index we have 1.
Still sum > k so, we again do sum = sum - arr[i] => sum = 1 => 6
i = i + 1 => 3

At i = 3, we have another 1. Since 6 > k So, we again do sum = sum - arr[i] => sum - 1 => 5
i = i + 1 => 4

And now, since sum is no longer > k, we are done with shrinking.

And next, we see that sum == k now, so that means we found yet another window with sum = 5. 

And length = j - i + 1 => 5 - 4 + 1 => 2

Is this length > previous maxLength = 4? NO. So maxLength remains unchanged.

We again move on to find next window so increase the size of current window by j++.

j = 5 + 1 => 6

At index = 6, we have 5. Sum = 5 + 5 => 10

Since 10 > k, that means again we have to now shrink the window. 

So, while(sum > k): shrink the window by removign ith element from sum and incrementing i

10 > k. At i = 4, we have 2. So, sum = 10 - 2 => 8 
Increment i. i = 4 + 1 => 5

8 > k. At i = 5, we have 3. So, sum = 8 - 3 => 5 
Increment i. i = 5 + 1 => 6

5 > k? NO. SO stop shrinking.


Now we check is sum == k? YES. That means [5] is also a valid window of sum k. Its length = (j - i + 1) => (6 - 6 + 1) => 1

Is 1 > maxLength so far? NO! so maxLength remains unchanged.


And since we reached end of array, we break our of while loop.


Finally, return maxLength = 4 as the length of largest subarray with Sum = k.



# NOTES

When the sum is > k then we shrink the window till sum is no longer > k i.e., till sum becomes <= k

This means, the if check for sum > k should be the first if check in our loop. That's because, afer we shrink the window, there are two cases
    -> Either sum will be < k
    -> Or sum will be > k

So we have to handle these cases after the sum > k if check only.

Otherwise, if we put the check for sum < k before the check for sum > k, then we have to again write the same code for checking if sum < k when we are done shrinking the window. And same for the check for sum == k.

This should be the Basic idea -


        sum = sum + arr[j]
        if sum > k:
                shrink the window by i++ till sum <= k
        
        if sum < k:
                increase the window size by j++
        else:
                check the length and select the maximum length
                increase the window size by j++

becase in both the cases when sum < k or sum == k we are incrementing j, we can make the code shorter -

        sum = sum + arr[j]
        if sum > k:
                shrink the window by i++ till sum <= k
        
        if sum == k:
                check the length and select the maximum length
        
        increase the window size by j++


