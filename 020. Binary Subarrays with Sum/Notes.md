# PROBLEM STATEMENT
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to array
    -> We have to find the subarrays
    -> We are given a condition for a valid subarray

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach

# VARIABLE SIZE SLIDING WINDOW - APPROACH

When we have problems where we have to subarrays with "exactly" the given sum. Then there is one thing we can do.

We can find how many subarrays have sum <= k and then find how many subarrays have sum <= k - 1

Then if we substract both, we will get how many subarrays have sum == k i.e., strictly equal to k

So we just need to create a separate method for calculating number of subarrays with at most "k" sum.

Then use that method for "k" as well as "k-1" sum and minus both results to get the required result.

# EXAMPLE

e.g. nums = 1 0 1 0 1, goal = 2

Lets see how many subarrays we have with sum <= 2

	[1], [1, 0], [0], [1, 0, 1], [0, 1], [1], [1, 0, 1, 0], [0, 1, 0], [1, 0], [0], [0, 1, 0, 1], [1, 0, 1], [0, 1], [1] => 14 Subarrays

Now find how many subarrays are there with sum <= 1
	
	[1], [1, 0], [0], [0, 1], [1], [0, 1, 0], [1, 0], [0], [0, 1], [1] => 10 Subarrays
	
So, subarrays with sum == 2 => 14 - 10 => 4

Because as we can see, the only subarrays that are not in the list of subarrays wth sum <= 1 are those that have sum == 2 i.e,

	[1,0,1], [1,0,1,0],[0,1,0,1], [1,0,1] => 4 Subarrays
	
	
Here is how sliding window approach helps us find subarrays with sum <= goal

	nums = 1 0 1 0 1, goal = 2
	
We start with i and j at 0th index. Since at jth index we have 1, sum = 1

	[0] is a valid subarray. So we found one subarray here. Count = 1

Now we increment j. j is now at index = 1. At index = 1, we have 0. Sum remains 1. Since 1 <= 2

	[1,0] is also a valid subarray with sum <= k So Count = 2
	
Now we increment j again. j is now at index = 2. We have 1. So sum becomes 1 + 1 => 2 Since 2 <= 2
	
	[1,0,1] is also a valid subarray with sum <= k So Count = 2
	
Again we increment j. j is now at index = 3. At index = 3, we have 0. So sum remains 2 and  2 <= 2

	[1,0,1,0] is also a valid subarray with sum <= k So Count = 2
	
Finally, j becomes 4. We have 1 so sum => 2 + 1 => 3 here, sum became > 2 so we have to shrink the window. We increment i. At ith index we had 1 so that also gets substracted from sum. Sum becomes 2. And since 2 <= 2
	
	[0,1,0,1] is also a valid subarray with sum <= k So Count = 2 So count = 4
	
And our loop ends.

But wait. What about other subarrays?

From [1] at i = 0, j = 0, we got only one subarray. But that's not same for others.

If [1,0] is a valid subarray when i = 0, j = 1, then [1,0]  and [0] are also valid. Which are subarrays of [1,0]
Note that we did not consider [1]  at i = 0 here since that is already considered in previous subarray.

Similarly, if [1,0,1] is a valid subarray when i = 0, j = 2 then [0,1], [1] and [1,0,1] are also valid (Do not that the [1] here is from index j = 2, not j = 0)

And since [1,0,1,0] is valid when i = 0, j = 3 then [1,0], [0,1,0], [0], [1,0,1,0] are also valid. 

Finally, since [0,1,0,1] is valid when i = 1, j = 4 then [0,1,0,1], [1,0,1], [0,1], and [1] are also valid. 


So here is what we got

	i = 0, j = 0 => 1 subarray
	i = 0, j = 1 => 2 Subarrays
	i = 0, j = 2 => 3 Subarrays
	i = 0, j = 3 => 4 Subarrays
	i = 1, j = 4 => 4 subarrays
	
	So basically, we get j - i + 1 subarrays from a particular subarray if it is valid. 
	j - i + 1 is basically the size of current window that is valid
	
	And that's why we do count += j - i + 1 