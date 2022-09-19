# PROBLEM STATEMENT

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

# EXAMPLE

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> Given a string
    -> We want to find the size of longest substring with same characters
    -> The condition is given (We can do at most K replacements)


# VARIABLE SIZE SLIDING WINDOW - APPROACH

This problem can be rephrased as - 

	Given a string s, return the length of longest substring containing same characters after at most k character replacements 


As we know, for a sliding window approach, one thing that we need is a condition based on which a window can be valid or invalid.

So the main idea is to first figure out that condition from the problem statement.

Basically, we want to return the length of the longest substring such that all the characters in it are the same after we replace at most k characters in it. 

e.g.  s = "ABAB", k = 2

This means, any window in which we can replace at most 2 characters to make all the characters same is a valid window. 

e.g. "AB" is a valid substring because in this, we can replace "B" to "A" to get "AA". So number of replacements we did = 1 which is <= k
Similarly, "ABA" is also a valid subtring because we can again replace "B" to "A" to get "AAA". So number of replacements = 1 <= k
And similarly, "ABAB" is also valid because we can replace two "B" to two "A" or vice versa (since both have same count) to get "AAAA" or "BBBB" so in this case, we did 2 replacements and 2 <= k

SO, the longest substring was "ABAB" and so we return its length i.e., 4.

This means, any substring is a valid substring if the number of replacements that we can do is <= k.

So now you might think - How to know what are the number of replacements?

Just take this case ->  s = "AABABBA", k = 1

Here, we will see that "BABB" is the longest  substring because we can replace one "A" to "B" and since we did only one replacement and 1 <= k, it is valid.

	Why we did not replace "B" to "A"? 
	That's because "B" occurs more number of times than "A" and since we want all characters to be same in a substring after replacement, 
	that means it is better to replace all the characters that occur less number of times than the one that occurs the most.

So, in "BABB", B occurs 3 times and the total length of this substring is 4

That means, we can replace 4 -3 = 1 character in this substring so that all the characters are "B" in this substring.

This means, we got a condition as - 

		
			Length of Substring - Highest Frequency of a character in substring = Number of Replacements we have to do
			
			Because, Length of Substring - Highest Frequency of a character in substring will give us the number of less occuring characters
			
e.g. even if we had "BABZ", here as well, "B" occurs twice so we would only consider replacing "A" or "Z" to "B" and not "B" to "A" or "Z".