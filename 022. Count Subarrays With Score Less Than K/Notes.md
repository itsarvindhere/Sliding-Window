# PROBLEM STATEMENT

The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.

Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to array
    -> We have to find the number of subarrays
    -> We are given a condition for a valid subarray

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach

# VARIABLE SIZE SLIDING WINDOW - APPROACH

For any subarray or window to be valid, its score should be < k

    Score = Sum * size of window

As we know, 

    Size of window = j = i + 1

So that means all that we need to keep track of is the sum so far in the window. 

And if the condition is satisfied, count is incremented by the size of current window because if a window is valid, that means its subarrays are also valid.

