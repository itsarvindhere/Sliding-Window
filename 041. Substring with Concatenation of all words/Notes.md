# PROBLEM STATEMENT

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.


# FIXED SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given a problem related to a string
 -> We want to find a substring of length = total length of words
 -> And we want to return an array of starting indices of valid substrings

# FIXED SIZE SLIDING WINDOW - APPROACH

How did we get to know that we only want to look at substrings of size = sum of length of each word in words list?

e.g. 

        s = "barfoothefoobarman", words = ["foo","bar"]

How many words are there -> 2
What is length of each words -> 3

Since we want a substring which contains the concatenation of all the words in words list, that means it should be of length = 2 * 3 => 6

So the window size is fixed. 


Also, notice that problem statement says - "concatenation of any permutation of words"

It does not say permutation of each individual word. This means the individual word in the words list will remain in the same order. Only the overall order in the words list can change. e.g.,

    words = ["foo","bar"]

So there are only two cases -> either foo comes before bar in a substring or bar comes before foo.

We are not concerned with permutations of each individual word here e.g. "oof" or "ofo" or "foo" etc. That is not the case.

That means, as soon as we get a window of size = (length of words * individual word length), we need to check if it has the words present in the words list. For that, we can check its substrings of size = individual word length.


e.g.  s = "barfoothefoobarman", words = ["foo","bar"]
So we need to check each window of size = 6.

    First we get "barfoo". We check its substrings of size = length of each word in words list. 
    So we check is "bar" present in the words list? YES it is. 
    Is "foo" present in the words list? YES it is.
    So yes, "barfoo" is a valid substring so put its starting index in output.
    Next, we get "arfoot" It is obviously not valid since words of length 3 out of it as "arf" and "oot" which are not present in words list.

And so on...