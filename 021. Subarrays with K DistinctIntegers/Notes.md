# PROBLEM STATEMENT

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

e.g.  nums = [1,2,1,2,3], k = 2

Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Since there are 7 subarrays, return 7.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to array
    -> We have to find the number of subarrays
    -> We are given a condition for a valid subarray

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach


# VARIABLE SIZE SLIDING WINDOW - APPROACH

The Simplest way to find how many subarrays have "exactly" K something is -

	 Number of Subarrays with At Most K something - Number of Subarrays with At Most K - 1 Something
	 
And this way, you can solve a lot of similar problems in sliding window. 

Lets understand how it works with an example.

		nums = [1,2,1,2,3], k = 2
		
So we want to return how many subarrays have exactly "K" distinct integers

Lets find how many subarrays have "At Most" K distinct integers. At most means number of distinct integers in a subarray should be <= K

So, we can see the valid subarrays with distincts <= K are -
	
	[1], [1, 2], [2], [1, 2, 1], [2, 1], [1], [1, 2, 1, 2], [2, 1, 2], [1, 2], [2], [2, 3], [3] => 12 Subarrays
	
And now do the same but for K - 1 i.e., find number of subarrays with distincts <= K -1

So, we can see the valid subarrays with distincts <= K - 1 are -
	
	[1], [2], [1], [2], [3] => 5 Subarrays

And so, Number of Subarrays with Exactly K different integers are -> 12 - 5 => 7

These subarrays are - 

	[1, 2], [1, 2, 1], [2, 1], [1, 2, 1, 2], [2, 1, 2], [1, 2], [2, 3] => 7 Subarrays
