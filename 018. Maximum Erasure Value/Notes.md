# PROBLEM STATEMENT

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

EXAMPLE:  nums = [4,2,4,5,6]

The subarrays with unique elements and their sum :

    [4,2] -> 6
    [2,4] -> 6
    [2,4,5] -> 11
    [2,4,5,6] -> 17
    [4,5,6] -> 15

So, the maximum sub subarray with unique elements is [2,4,5,6] so return its sum => 17


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to array
    -> We have to find the subarra
    -> We are given a condition

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach

# VARIABLE SIZE SLIDING WINDOW - APPROACH

This problem statement can be rephrased as -

    Given a positive integers array nums, return the maximum sum subarray, given it has unique elements only

And now, this problem becomes pretty straightforward, right? Now we just need to keep track of each element and its count, as well as the sum of current subarray.

If we add some element into the dictionary and it is already present, that means the subarray is no longer having all uniques so we have to shrink the window until we get a unique elements subarray. 

And along with that, we also keep calculating the sum so far and finally update the maxSum if the current window has a greater sum.

This problem is a variation of the Problem in which we had to find the length of longest substring with no repeated characters. There, we had a string and here, we have an array.