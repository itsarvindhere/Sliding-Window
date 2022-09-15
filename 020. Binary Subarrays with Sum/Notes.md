# PROBLEM STATEMENT
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to array
    -> We have to find the subarrays
    -> We are given a condition for a valid subarray

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach

# VARIABLE SIZE SLIDING WINDOW - APPROACH

When we have problems where we have to subarrays with "exactly" the given sum. Then there is one thing we can do.

We can find how many subarrays have sum <= k and then find how many subarrays have sum <= k - 1

Then if we substract both, we will get how many subarrays have sum == k i.e., strictly equal to k

So we just need to create a separate method for calculating number of subarrays with at most "k" sum.

Then use that method for "k" as well as "k-1" sum and minus both results to get the required result.