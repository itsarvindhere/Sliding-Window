# PROBLEM STATEMENT
A string is considered beautiful if it satisfies the following conditions:

    1. Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
    2. The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).


For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a string problem
    -> We have to find the length of longest substring
    -> And we have the condition for a valid substring

So yes, this is a variable size sliding window problem.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

This question is a variation of previous problem in which we had to find the length of longest alphabetically continuous substring.

In this one, instead of checking for alphabetically continuous, we need to check alphabetical vowel order. 

But an extra condition here is that all the vowels need to appear in the substring at least once. Since there are 5 vowels, it means a valid substring should have 5 distinct characters. Hence we need to keep track of distincts too.

And rest is the same template as previous problem.

In previous problem, current character needed to be one more than previous.


In this problem, the current character can either be same as previous or greater than previous (in terms of ascii value).

If same, distincts remain same. But if it is different, we got a new distinct so distincts are incremented.

And we update the maxLength only if current window has 5 distinct characters.