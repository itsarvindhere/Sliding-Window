# PROBLEM STATEMENT

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# FIXED SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given a string related problem
 -> We are also given the size of a substring/window
 -> We have to maximize the number of vowels in each window of size k

Since we are given the size of window, this means window will be of fixed size at any point so this problem can be solved using the Fixed Size Sliding Window Approach.

# FIXED SIZE SLIDING WINDOW - APPROACH

We just need to first make the window size = k and then maintain it for the rest of the iterations.

And for each window of size k, we need to see how many vowels are there. If they are more than previous max, then update the max.

And finally return the maxCount.