# PROBLEM STATEMENT

Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

e.g.
    Arr = [2,5,1,8,2,9,1]
    N = 7
    K = 3 (Window Size)


# IDENTIFICATION OF SLIDING WINDOW

 1. It is a question of an array
 2. Subarray is mentioned
 3. Length of Subarray is given
 4. Largest Sum of a subarray of length K is to be returned

Hence, this is a problem that can be solved using Sliding Window Approach

# SLIDING WINDOW APPROACH

So, we have to take each K length subarray and find its sum. And then we have to return the maximum Sum.

e.g. in Arr = [2,5,1,8,2,9,1], subarrays of size 3 and their sum is - 

        [2,5,1] -> 8
        [5,1,8] -> 14
        [1,8,2] ->  11
        [8,2,9] -> 19   <-- This is the maximum SUM
        [2,9,1] -> 12

Output = 19

Since we are given K = 3, we will make a Window of Size 3

This means we will have some start index and some end index for a window, right?

Lets say start index = i and end index = j

        Arr = [2,5,1,8,2,9,1]

Suppose,  i = index 2
          j = index 4

So what is the size of this window? Just by looking we see the window is [1,8,2] and it is of size 3. How to find the size from these indexes?

If we do j - i then it is 2. That means, the size of window is (j - i + 1) which is equal to 3. 

So, we can use (j - i + 1) to make sure size is K and not less or more than K.

        Arr = [2,5,1,8,2,9,1], k = 3

Initially, i = 0, j = 0

So window size => j - i + 1 => 1 

Since we are given K = 3. That means our curent window size can be increased. So we increment j = j + 1

Now, i = 0, j = 1. Window size = 2

Again, 2 < 3 so it can be increased

i = 0, j = 2. Window size = 3

So here, we got a window of size K. 

And now, we can maintain this window size so that we can now just slide our window and no need to worry about the size.

Because it makes no sense to again do the same calculations for next set of numbers.

How to maintain window size in each iteration? WE an simply add a new number to end and remove a number from starting.

i.e., increment i by 1 and j by 1

    Arr = [2,5,1,8,2,9,1], k = 3
    If initially i = 0. j = 2 . Window = [2,5,1]
    
    then when we do i++ and j++

    i = 1, j = 3. Window = [5,1,8]
    We also need to minus the first element of previosu window i.e., 2 from the sum that we got for current window
    
     So, the window size remains 3 only i.e., it is maintained.