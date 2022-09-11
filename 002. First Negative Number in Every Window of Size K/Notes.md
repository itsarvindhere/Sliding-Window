# PROBLEM STATEMENT

Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

e.g.  array = [-8, 2, 3, -6, -10] and k = 2

So, subarrays with size 2 are ->

    [-8,2] -> First negative number -> -8
    [2,3] -> No Negative number so for this -> 0
    [3,-6] -> First negative number -> -6
    [-6,-10] -> First negative number -> -6

So, output list will be [-8,0,-6,-6]

The basic idea is that if a window has multiple negative numbers, return the first one from that window. If there are no negatives, return 0 for that window. If there is only one negative number, that particular number is the output for that window.

# BRUTE FORCE APPROACH

Suppose array = [-8, 2, 3, -6, -10]

If we try a brute force approach, we will use two nested loops such that i starts at 0 and j goes from i to k i.e., window length.
And then we check each element in the window and whichever is the first negative, we put in output array. So far it sounds fine.

But then in next iteration, when we are at next window, we again check for each element from the beginning of window, even though we have already checked for all the elements except the one new element that we added at the end. So, we are doing repetitive work here and so, sliding window approach can help to optimize the solution.


# SLIDING WINDOW APPROACH

Since we are given an array, window size, and also condition. It is pretty straightforward that this is a question of sliding window.

So how are we going to approach this problem?

Here, apart from the output array that we have to return, we will also need another list to store the negative numbers for each window.

        array = [-8, 2, 3, -6, -10]

So, just like how we did in previous problem, the basic idea will be the same. i.e., i and j will initially be 0, then we start a while loop till j < N, then we increment j if the window size is not yet equal to k etc.

The main thing is, for each window, till we have not reached the window size, we also store the negative numbers in that window in a list.

e.g.    array = [-8, 2, 3, -6, -10], k = 2

Initially, i = 0, j = 0

Now loop starts. We are at index 0 and we see that the number at index j is -8 which is negative. SO we put it in a list

    Negative list = [-8]

Since window size currently is j - i + 1 => 1 != k

So we increment j. j = 1 now.

Another iteration runs. We check if element at index j is negative or not. Since 2 is not negative, we will not put it in negative list.

Now we again check window size. j - i + 1 => 1 - 0 + 1 => 2 = k

Since window size is now k, it means for this window, the first negative number will be the first number in the negative list. 
If the list was empty, that means for this window, there is no negative number hence in that case we would put 0 in output list.

So, we put -8 in output for the above window.

Next, we want to increment both i and j. 

Since we are sliding the window to right, that means the first element of previous window will be discarded. In simple words, since next window is [2,3] It means -8 will be discarded from this window and so, we have to discard it from our negative list too.

So, before incrementing i, we can check if the element at i index is the first element of negative list. If yes, then slice the array so that -8 is removed.

And this same process repeats till be reach the end of array.