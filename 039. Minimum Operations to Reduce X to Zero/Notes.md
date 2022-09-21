# PROBLEM STATEMENT

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# EXAMPLE

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.


# VARIABLE SIZE SLIDING WINDOW PROBLEM - IDENTIFICATION AND APPROACH

How is this a variable size sliding window problem? We are not asked to find length of a subarray and also, we do not remove numbers from array in order. We either remove from start or end.

So, if we cannot find minimum number of elements to remove, can we find maximum number of elements to not remove?

Think it like this.

    We remove elements from either start or end. That means, if at the end, the array has some elements left, then that must be a subarray, right?

    e.g. [1,1,4,2,3]

    If we remove 3 first. Our array becomes [1,1,4,2]
    Now since we want sum = 5 of removed elements, we now remove 2. so 3 + 2 = 5 == x
    Now array becomes [1,1,4,2]

    And this is a subarray of [1,1,4,2,3]

    So how can we find this particular subarray using sliding window? Because if we can find how many elements we are not going to remove, we can find how many we will remove by simply doing - 

        Elements removed = (total elements in array - number of elements to not remove)

    
    We removed 3 and 2 because their sum was equal to x. This means, all the remaining subarray will have 
    
        sum = (total Sum of array - x)


And now, this problem can be divided into 2 parts -> 

    1. Find the longest subarray of elements such that sum = (total array sum - x)
    2. Now we can find, Elements removed = (total elements in array - length of longest subarray of elements such that sum = (total array sum - x))

So for part 1, we use variable size sliding window approach.