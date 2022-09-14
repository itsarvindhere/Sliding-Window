# PROBLEM STATEMENT

Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

EXAMPLE:

        S = "aabacbebebe"
        K = 3

We have to find the longest substring which has exactly 3 unique characters in it.

If we see in the string above, substrings with exactly 3 uniqye characters are - 

        "aabac" -> 3 Unique characters are "a", "b" and "c"
        "abac" -> 3 Unique characters are "a", "b" and "c"
        "abacb" -> 3 Unique Characters are "a", "b" and "c"
        "bacb" -> 3 Unique Characters are "a", "b" and "c"
        "acb" -> 3 Unique Characters are "a", "b" and "c"
        "cbebebe" -> 3 Unique Characters are "b", "c" and "e"
        and so on...

Out of all these, the longest substring with 3 unique characters is "cbebebe" which is of length = 7. Hence, we return 7 as the output.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> The problem is related to a String
    -> We want to find a Substring
    -> K is given which is the number of unique characters

So, this is a problem related to Variable Size Sliding Window because we are not given the size of the window, rahter we have to find the maximum size based on the given condition.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

Here is the general format of the Variable Size Sliding Window that we will follow - 


        while(j < size):
            //Calculations

            # If calculations exceed the condition that means we have to shrink the window
            if(condition exceeded):
                while(condition exceeded):
                    condition -= arr[i]
                    i += 1
            
            # If condition is matched then store the result
            if(condition matched): 

            // Store the answer

            # Increase the window size
            j += 1


Here, condition is -> K unique Characters

This means, we need a way to keep track of the unique characters in current window. We can use a hashmap for that as it will keep the occurance of each character in a window.

And to get unique count, we can us the length of map for that.

So here are the steps -

        1. Put the jth character in the map. If it is already in map, just increment its count, otherwise add it in map with count = 1
        2. Now check if the size of map is > k. If it is, then that means we need to shrink the size of current window. So for that, we have to remove all the calculations we did for the ith character. That is, decrease the count of ith character by 1. If the count becomes 0, that means there is no such character anymore in our new window so we can remove that character from map too so that number of unique also comes down by 1 when we check length of map.
        3. If the length of map is same as K, that means the current window has exactly K unique characters so in that scenario, we can save the length of current window in a variable if it is greater than previous maxLength.
        4. And finally, we increase the window size by incrementing j

And the above steps repeat till we reach the end of String.