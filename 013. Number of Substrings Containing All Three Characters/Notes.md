# PROBLEM STATEMENT

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a string problem
    -> We have to deal with substrings
    -> And we have to return count of substrings
    -> The condition is also given

Since, we are not given the size of window, that means it is a problem related to Variable Size Sliding Window.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

First, we want to have a way to keep track of count of a, b and c in the current window. That can be done using a map easily. Because we are told that the string consists of only a,b, and c. That means we can simply keep a map with counts of a,b,c initialized as 0.

Next, we need to think what we want to do when for a current window, all three characters are present at least once.

i.e., if count of each character is > 0 then what to do?

One thing that instantly comes to mind is to increment the output that we are eventually returning. But that won't give correct results. Why?

    Because first we will get "abc" and count will be 1
    Then we will get "bca" and count will be 2
    then we get "cab" and count will be 3
    and finally we get "abc" and count will be 4

So we are getting only the length = 3 substrings using this. What about substrings such as "abca" "abcab" "abcabc" "bcab" bcabc" "cabc" ?

That's why we need to incrase the count for a particular valid window in a special way.

    consider this string -> "abcabc"

When we will be at index 2, then our window will be "abc" and this will be a valid substring because it has all the characters at least once. But, think about what will happen if we add the characters outside of this window to this string. Will that affect its validity? No it wont!

after index = 2, the string left is "abc"

so, if we take our current window "abc" and took all the substrings of string after this window i.e.,  "abc" what we get?

We get "abca" "abcab" abcabc" 

And sicne "abc" itself is also a valid substring that means in total, for "abc" window, we can get 4 valid substrings when we include the substrings of the rest of the string outside the window too.

Now how to get this 4? This is just length of string - jth index

Here, length = 6 and j = 2 so count += length - j => 4 valid substrings


Similarly, for the window between i = 1 and j = 3 we have "bca" which is valid in itself and if we add all the substrings of the string after this window then we get -

    "bcab", "bcabc"

So, including "bca" itself, we have in total 3 substrings

i.e., length - j => 6 - 3 => 3 valid substrings

Similarly, for window between i = 2 and j = 4 we have "cab"

And again lets generate all the strings for "cab" abd "c" which is the only character outside of this window

So we get "cabc" and that's it.

This means, including "cab" as well, we have 2 substrings here. 

i.e., length - j => 6 - 4 => 2 valid substrings


And finally, we have the last window between i = 3 and j = 5

The substring is "abc" Since there are no characters after this window, that means for this we get 

length - j => 6 - 5 => 1 valid substring


Total => 4 + 3 + 2 + 1 => 10 substrings that satisfy the given condition.


Hence, return 10.