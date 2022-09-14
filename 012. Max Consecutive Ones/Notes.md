# PROBLEM STATEMENT

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


EXAMPLE: 
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

So basically, we want to find those subarrays that contains 2 or less than 2 zeros. And we want to return the maximum length out of those. 

e.g. in above array, these are the subarrays with at least 2 zeros
    [0]
    [0,0]
    [1,0,0]
    [1,1,0,0]
    [1,1,1,0,0]
    [0,0,1]
    [0,0,1,1]
    [0,0,1,1,1]
    [0,0,1,1,1,1]
    [0,1,1,1,1,0]

So, the longest subarray are two and both have length = 6. So, for the above array and k = 2, output = 6


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

How is this a question related to Variable Size Sliding window?

    -> We are given an array
    -> We have to deal with subarrays
    -> We are given a condition that zeros cannot exceed k
    -> We have to return length of largest subarray

So yes, this is a problem that can be solved using Variable Size Sliding Window.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

The approach is quite straightforward. Since we know that we just have to find all those subarrays that have zeros <= k that means, wejust need to follow the general template for variable size sliding window.

Whenever we come across a 0, we increment count of zeros. And in case count becomes > k, we will make sure it comes back to k or less than k to make sure our condition remains satisfied.

In this way, we calculate length of each subarray and get the max length out of that.