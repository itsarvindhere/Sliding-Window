# PROBLEM STATEMENT

Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.

# EXAMPLE  

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

# FIXED SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given a string
 -> We have to find maximum number of occurances of a substring
 -> Size range of substring is given
 -> Condition to choose a valid substring is given


# HOW IS THIS A FIXED SIZE SLIDING WINDOW PROBLEM?

You might be thinking - If there is no fixed size given then how is this a fixed size sliding window problem? We only have a range of valid sizes.

WEll, we have to figure out the fixed size from the range given.

In fact, the maxSize is something we will never consider at all! Why? 


Understand this example -

			s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 4
			

Lets first see how many substrings are there wth size = maxSize

	We have only one i.e., "aaaa" 
	
But if there is 1 substring of size = maxSize, doesn't that mean there is at least the same number of substrings of size >= minSize and < maxSize? Since minSize <= maxSize.

And indeed there are two substrings with size = minSize

	"aaa" and "aaa"
	

In other words, if we have a substring of size = minSize then it has a bigger possibility of occuring multiple times than a substring that has a larger size. 

The substring with size = minSize will occur either the same number of times as maxSize substring or more than that. So that means, considering maxSize in code is a waste of time. 

Here, the lowest limit of size is minSize and that's why if we can find a substring of that size, it has a higher chance to occur more than any substring with size > minSize and <= maxSize

That's why, we will only consider substrings of length = minSize and well, we got our fixed Size.

So we will maintain a window of length = minSize and then for each window check if unique characters are <= maxLetters. If yes, we can consider that substring to be valid and update its count.

In the end, just pick the highest count and return that.

So to simplify this problem -

    Given a string s, return the maximum number of ocurrences of a substring of size = minSize with at most "maxLetters" unique characters