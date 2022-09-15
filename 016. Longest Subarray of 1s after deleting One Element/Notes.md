# PROBLEM STATEMENT

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

EXAMPLE: nums = [1,1,0,1]

Here, we can remove the 0 at the index = 2 to make the array as [1,1,1] So, the length of longest subarray of 1s after deleting one element is 3

    num = [0,1,1,1,0,1,1,0,1]

Here, we can delete the zero at 4th place and then we get the longest subarray as [1,1,1,1,1] which is of size 5 so return 5.


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to array
    -> We have to find the length of longest subarray
    -> We are given a condition

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach

# VARIABLE SIZE SLIDING WINDOW - APPROACH

The problem definition can be simplified as -

	Given a binary array nums, return the longest subarray that has at most one 0
	
And well that's pretty much it. 

Now we just need to keep track of all the subarrays that have only one zero and maintain the maximum length out of those.

And finally, because we want to return the length without including the one zero, we just do maxLength - 1