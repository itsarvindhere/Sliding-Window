# PROBLEM STATEMENT
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

# EXAMPLE

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

# FIXED SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a string related problem
    -> Since we want to find permutation of s1 in s2, that means we want a subarray in s2 which is a permutation of s1
    -> And that also means, the subarray length will be = length of s1

So yes, this is a fixed size sliding window problem

# FIXED SIZE SLIDING WINDOW - APPROACH

This is almost the same problem as Count Occurances of Anagrams.

In that, we had to counts how many times an anagram of s1 occurs in s2.

Here we just need to check if the anagram is present in s2 then simply return True.