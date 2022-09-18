# PROBLEM STATEMENT

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.


# EXAMPLE

Input: nums = [8,2,4,7], limit = 4
Output: 2 

Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 

Therefore, the size of the longest subarray is 2.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are Given an Array
 -> We want to find the longest subarray
 -> The condition is also given

So yes, this is a variable size sliding window problem.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

This problem is quite similar to the Sliding Window Maximum Problem because in this one too, we will make use of deque to keep track of useful elements that may become maximum for any future window.

Here, as we also want to know the smallest element in a window, we want another deque to keep track of the useful minimum elements.

And well, that's pretty much the main thing in this problem. Rest is the general variable size sliding window template.