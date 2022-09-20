# PROBLEM STATEMENT

Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.

For eg. A = aabcbcdbca, then the result would be 4 as of the smallest window will be dbca.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> Given a String problem
    -> We need to find the smallest valid sustring length
    -> The condition is also given

# VARIABLE SIZE SLIDING WINDOW - APPROACH

This problem is somewhat similar to the Minimum Window Substring. In that, we had to return the substring but here, we just need to return the min length. So that's one step less in this problem.

Also, in that, we had an extra string given but here, we will get the extra string out of the given string itself.

It is given that the task is to find a smallest substring such that it has all the characters of the original string at least once. 

So, we can keep a counter which initially has 0 count for each character. And the length of counter will be the number of distinct characters in a window.


And this way, we just need to track the count such that as soon as a character's count becomes 1, that means we now have one less character to find in this window so distincts is decremented.

In similar way, when we increment ith pointer, if a character's count becomes 0, that means we have one extra character to find so distincts is incremented