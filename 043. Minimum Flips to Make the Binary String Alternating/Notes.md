# PROBLEM STATEMENT

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

    Type-1: Remove the character at the start of the string s and append it to the end of the string.
    Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
    Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.


# EXAMPLE

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

# FIXED SIZE SLIDING WINDOW - IDENTIFICATION AND APPROACH

We are given a binary string and we want to make it alternating. Alternating means each 0 after each 1 and 1 after each 0. e.g. for a binary string of length = 3, we have two valid alternating string -> 101 and 010. In fact, for every length, there are only two valid alternting strings which is obvious because there are only two types of numbers in a binary string - 1 and 0.

For a moment, forget that type-1 operation exists. Just think that we are given a string and we can flip a bit. We want to find minimum number of flips we can do so that this string is alternating. How will you do it? Will you take each bit, flip it and check if that makes string alternating? Ofcourse not. 

Because we know that for any length, there are only two valid alternating strings, we can simply compare each position with each valid string. And if the number at that position differs, we need to flip. In other words -

		Minimum Number of Flips = Minimum Number of differences between given string and valid strings

		lets say s = "111000"

Since length is 6, what are the valid alternating binary strings of length 6? They are 
		
			valid1 = "101010"
			valid2 = "010101"

So, lets compare s with valid1 first

			s =      "111000"
			valid1 = "101010"
			
			For each position in s, check what is the value at same position in valid1. If they are not same, we need to flip.
			
			So we get differences = 2
	
Now lets compare s with valid2
			
			s =      "111000"
			valid1 = "010101"
						
			We get differences = 4
			
So that means, we can simply flip 2 bits to make the string alternating such that it starts with 1, instead of flipping 4 bits such that it starts with 0.

Now we add in the type-1 operation. It says that we can take a character from beginning of string "s" and add it to the end of it in order to minimize the flips. What that means?

	Lets say we performed type-1 operation once on s = "111000"
	Then the first "1" will be moved to end. So string will become "110001"
	
	And now again, we have to do the same thing as above 
	i.e., compare it with valid1 and valid2 to see which one results in least difference.
	
What is the maximum number of type-1 operations we can do? It is equal to length of string. Why? Because if we take the whole string and append it to itself, that means we get the same string in return.

	s = "111000" 
	1 type-1 operation, s = "110001"
	2 type-1 operations, s = "100011"
	3 type-1 operations, s = "000111"
	4 type-1 operations, s = "001110"
	5 type-1 operations, s = "011100"
	6 type-1 operations, s = "111000" => Back to original
	
So it makes no sense to go above 6 in this case as we would be doing the same work again. 

So that means, instead of manually taking each character and moving it to end, why not we double the given string "s" .

	s = "111000" to s + s
	such that new s => "111000111000"
	
	And now, each window of size = 6 represents each type-1 operation.
	
	First window of size 6 -> "111000"
	Second window of size 6 -> "110001"
	Third window of size 6 -> "100011"
	Fourth window of size 6 -> "000111"
	Fifth window of size 6 -> "001110"
	Sixth window of size 6 -> "011100"
	Seventh window of size 6 -> "111000" => Back to original
	
So we had to do no extra work to take each character from beginning and move it to end.

And now. Just think how we were comparing the string with valid1 and valid2.

		s =      "111000"
		valid1 = "101010"
		Differences = 2
		
When we take a character out from "s" and move it to end, then that means, we need to do the same with valid1 right? Because we won't be recalculating the whole difference again when only one character has changed. 

In other words, as we slide the window, all that we are doing is just check the one extra character that we added at the end and also before sliding the window remove all the calculations for that character.
		
And the rest, is a general sliding window template.

You might be thinking does type-1 operation even helps in minimizing the flips? Because for above example, even if we don't do type-1 operation, we get 2 minimum flips. And after doing as well, we get 2.  Yes, you are right. For some strings, this doubling of strings is not required at all. That's the case with even number of characters in a given string. So, if length of string is even, there is no need to double the string. But  when there is an odd number, we may get a minimum value after doing type-1 operation. Try with s = "11100" you will understand.

Because in "11100" if we take four characters from beginning and append them to end we get "01110' ANd now, all we need to do is 1 flip for the 1 at the center to make it "01010". So minimum Flips = 1

But had we not done the type-1 operation at all, then minimum flips would be 2. i.e., flipping the 2nd "1" and last "0" to get "10101"