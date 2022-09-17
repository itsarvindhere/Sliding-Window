# PROBLEM STATEMENT

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 -> We have a string related problem
 -> We are asked to find maximum length of substring
 -> We are given the condition


So yes, this is a problem related to Variable Size Sliding Window

# VARIABLE SIZE SLIDING WINDOW - APPROACH

The problem statement can be rephrased as -

    Find the length of longest substring with cost of replacing characters <= maxCost

And boom! It now sounds like a super simple problem, right?

This now becomes a simple variable sliding window problem where we just need to keep calculating the replacement cost for each character we include in a window and if the cost becomes greater than maxCost, then we need to shrink the window from left.

And if condition is met, just calculate the maximum length by comparing previous maxLength and current window length