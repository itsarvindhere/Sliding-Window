# PROBLEM STATEMENT

Given a word 'pat' and a text 'txt'. Return the count of the occurences of anagrams of the word in the text.

e.g. txt = forxxorfxdofr, pat = for

In this string, the following substrings exist of length = 3

    for, orx, rxx, xxo, xor, orf, rfx, fxd, xdo, dof, ofr

Here, if we see, "for", "orf" and "ofr" are the occurances of anagrams of "for" in this string.

Anagram means - a word formed by rearranging the letters of another. So, anagrams of "for" can be - "for", "ofr", "rfo", "orf" and so on.

# IDENTIFYING SLIDING WINDOW APPROACH IN THIS

We are given a problem regarding string. But the problem does not mention "k" or "substring". 

But, because we are given a pattern and we have to see how many times the anagrams of pattern exist, that means, if the pattern occurs in a string, then it will occur in a continuous manner. And the length of occured anagram will be same as length of the pattern. 

This means, because the pattern will be continuous, then we can have look at every substring. And because we talked about substring here, that means we can use sliding window here.

The window size is actually length of the pattern given to us because we want the substring length to be same as length of pattern Only then we can see if it is anagram or not.

# SLIDING WINDOW APPROACH

  txt = "aabaabaa"
  pat = "aaba"

So, window size = length of pat => 4

How do we check if the current window has the anagram of "aaba"?

We have to check whether the count of each letter in a window is the same as count of each letter in the pat.

e.g. txt = "aabaabaa"
     pat = "aaba"

The first window of length 4 will be   "aaba". Since the count of each letter (a : 3 and b:1) is the same as count of each letter in pat, it means this is an anagram.

Now our window becomes "abaa". Again, the count is same. 

next is "baab" Here, since a occurs twice only and b occurs twice, that is not same as for our pat. So this is not a valid anagram.

Next is "aaba". This is also an anagram

Next is "abaa" and this is also an anagram.

So, for the above example, there are 4 anagrams of the string "aaba".


To simplify this, we can have a variable equal to number of distinct characters in "pat". So that, if this variable becomes 0 for any window, that means that window is a valid anagram.


And before sliding the window, we just take the first character of current window and if it is present in the map, increment its count since it will be removed from next window as we slide it to right. ALso, we need to increment the variable we declared for distincts if the count of that character is map is now 1.


