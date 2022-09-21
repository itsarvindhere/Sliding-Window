# PROBLEM STATEMENT

An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.

Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

# EXAMPLE

    Input: s = "abacaba"
    Output: 2
    Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
    "ab" is the longest continuous substring.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a string problem
    -> We have to find the length of longest substring
    -> And we have the condition for a valid substring

So yes, this is a variable size sliding window problem.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

So, what are the conditions for a valid substring?

The only condition is that it should be alphabetical. That means, if previous character was "a" then nextwill be "b". It cannot be any other because the difference between "a" and "b" is 1. So, the next character needs to be 1 more than previous. 

And so, for every window, we check if current character is 1 more than previous, we can move to the next character. 

At the moment this condition is false, we know we have found one window and we need to start again from next window. So just calculate the length of current valid window and move on to the next window. 

And we can start out i and j pointers from 0 and 1 because we know the smallest possible length can be 1. Because each character in itself is alphabetic. 

            s = "abacaba"

So, initially, i = 0 and j = 1 which means i points to "a" and j points to "b"

And as we know, we need to keep increasing window size until current character is no longer 1 more than previous.

So we see that "b" is one more than "a" so we move ahead.  j becomes 2 so it points to "a"

Now we check. Is "a" one more than "b" ? NO! That means, adding "a" to this window makes it invalid. So, the valid window is from i = 0 to j = 1 i.e., size = 2. 

And to find next valid window, we will now set i to point at 2 i.e., "a" and j to point at 3 i.e., "c" and this going on....

At the end, we will get maxLength as 2.