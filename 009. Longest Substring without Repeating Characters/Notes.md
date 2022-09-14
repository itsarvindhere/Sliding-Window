# PROBLEM STATEMENT

Given a string s, find the length of the longest substring without repeating characters.

No Repeating Characters means All Unique Characters. So, this problem is a slight variation of Longest Substring with K Unique Characters.

EXAMPLE: s = "abcabcbb"

Here, the substrings without repeated characters are : 

    [a], [b], [c], [ab], [abc], [bca], [cab], [cb] etc..

    The longest substring without repeating characters are [abc], [bca], [cab] all of length = 3

    So output = 3

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given a string
 -> We have to find the length of longest substring
 -> The condition is given as well

So, this is a question that can be approached using Variable Size Sliding Window because in this, we have to find the size of window and we are given a condition.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

We will maintain a set that, as we know, only stores unique elements so we can check before we put a character in the set whether that character is already present or not.

We initialize an empty set and two pointers i and j which point to the 0th index

	s = "ababc"
		 i
		 j
		 
 Now, we check if the character at jth index is present in set or not. Since "a" is not present in the set, we can safely put it in the set and move further. We also keep checking the length in each iteration because as we know, even a 1 length substring can be the output.
 
 So we move on to the next index. j = 1
 
	s = "ababc"
		 i
		  j

At j = 1, we have "b". Is "b" present in set already? NO. That means we can safely put it in the set. 

So, the set now has ('a', 'b')

And length is now 2 because set always has unique characters in it so the length of substring = length of set. maxLength updated to 2.

We move to next index of j.

	s = "ababc"
		 i
		   j
		   
Now we get "a". We check if "a" is already present in the set. YES it is! This means, we have to shrink the window because until the "a" is already present in the set, we cannot consider another "a" in the current substring. So, until we no longer have "a" in set, we will keep removing items from the set at "i" index and then increment the "i" index to shrink the size of window.

Because in this case, "a" is the ith character to we remove it in first iteration itself when we check while(c in uniques). 

	s = "ababc"
		  i
		   j
		   
And now that set does not have 'a', we insert the 'a' that we got at jth index.

i is now pointing to the index 1. And set looks like ('b', 'a'). Length is 2 so maxLength is not updated since previous maxLength was also 2. 

j is incremented. Now, j points to index = 3

	s = "ababc"
		  i
		    j

At index 3, we have b. Do we already have "b" in the set? YES! That means, we need to remove the "b" first and only then we can insert "b" again to make sure there are only uniques in the current substring.

So, until "b" is not removed, we keep removing ith index character from set and keep incrementing i.

	s = "ababc"
		   i
		    j
			
The set becomes ('a') which means now we can safely insert 'b'.  Set becomes ('a', 'b') And same story as above since length = 2

We again increment j. j points to index = 4

	s = "ababc"
		   i
		     j

At index = 4, we have 'c'. Is 'c' already present in the set? NO! So that is why we will put 'c' safely in the set and set becomes ('a', 'b', 'c')
Length = 3 which means we can now update maxLength to 3. 

And j increments. j points to index = 5 which means loop ends. And finally, we return 3 as the length of longest subarray with all unique characters.


# USING A DICTIONARY

We could've also done this problem using a disctionary instead of a set, just like the previous problem of K unique characters. The general format would have been like -

		while(j < n):
        #Character that we want to insert in dictionary
        c = S[j]

		#Insert the character
		dict[c] = 1 if not c in dict else dict[c] + 1

        #It the value in dict is 2 that means this character occurs twice in this substring so we need to shrink the window until this substring has this character only once      
        if dict[c] > 1:
            while(dict[c] > 1):
				dict[S[i]] -= 1
                i += 1

        # Now we can calculate the length safely as we took care of all uniques condition above
        maxLength = max(maxLength, j - i + 1)

        #Increase the size of window
        j += 1