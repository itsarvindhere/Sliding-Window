# PROBLEM STATEMENT

You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

# EXAMPLE

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> Given a problem related to a string
    -> We are asked to return the smallest substring length
    -> The condition is also given

So yes, this is a problem that can be approached using Variable Size Sliding Window.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

To use sliding window, we first need to do some calculations.

It is given that there are only four types of characters in string -  'Q', 'W', 'E', and 'R'.

And it is also given that there are chances that some characters may occur more than n/4 times. So first, we want to find those characters that are occuring extra times because only because of those characters our string is not balanced. 

So, we will first count the frequency of each character and then, we will check which one occurs more than n/4 times. And lets store those characters somewhere with their "extra" frequency. i..e, How many extra times they are occuring.


		s = "QQQW"
		
Here, if we count each character's frequency, we get : 

		counter = { "Q" : 3, "W" : 1, "E" : 0, "R" : 0 }

Ideally, since length of string is 4, each character should occur 4/4 = 1 times. But there are extra characters. So lets count those. 

		extra = {"Q" : 2 }
		
So we see that there is only one extra character which occurs 2 more than ideal frequency.
	
What this means? This means for a string to be balanced, these two "Q" need to be replaced by "E" and "R". In other words,

	The smallest substring to be replaced is the substring that contains 2 Qs
	
Hence, now we can use sliding window approach to find the smallest substring with 2 Qs. 

Obviously there will be scenarios whereas more than one character is extra. 

	e.g. s = "QQWW"
	
	In this case, extra = {"Q" : 1, "W ", 1}
	
So, this means, the smallest substring should have two distinct characters and each of those characters need to be present in "extra". That's why we used a "distincts" variable to keep track of distinct extra characters in each window.

As soon as distincts becomes 0, that window is a valid substring but we want the smallest possible window so we will shrink it until distincts are no longer 0. 