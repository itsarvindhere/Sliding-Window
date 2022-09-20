# PROBLEM STATEMENT
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string

# EXAMPLE

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given a string problem
 -> We are asked to find the smallest substring out of it
 -> The condition is also given

So yes, this s a Variable Size Sliding Window Problem.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

The main thing to understand is that a valid substring needs to have a character at least the same number of times as it appears in string 't'. It does not matter if it appears more than in "t". But the least count of it in a substring should be = count in "t".

For once, just assume that this problem asks us to return the length of minimum substring such that each character in string 't' is included in the substring (with at least the same frequency)

So if you think like this, then that means we just need to keep track of the count of the characters in 't' and the count in the current window. If at any moment, we see that current window has all the characters of 't' in at least the same frequency, then that window is valid so we can consider it if its length is smaller than previous window.

And if we found a smaller window than before, then we also keep track of its starting and ending index so that using those, later we can construct the substring that we want to return.

And at the end, just return the substring we constructed from the starting and ending indices.