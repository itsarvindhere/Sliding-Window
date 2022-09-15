# PROBLEM STATEMENT

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

EXAMPLE: target = 7, nums = [2,3,1,2,4,3]

In this array, the following subarrays have sum >= 7

    [2,3,1,2,4,3]
    [2,3,1,2,4]
    [2,3,1,2]
    [3,1,2,4,3]
    [1,2,4,3]
    [2,4,3]
    [4,3]

    And so on...

Finally, we will see that the smallest subarray with sum >= 7 is [4,3] and its length is 2. That's why for the above input, output = 2


# VARIABLE SIZE SLIDING WINDOW - INTRODUCTION

    -> We are given an array
    -> We have to find length of smallest subarray
    -> Condition is given on the basis of which we want to find the length of smallest subarray

So clearly, this is a problem related to Variable Size sliding window because we are not given a fixed size, rather we have to find a minimum size.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

The problem statement can be simply put as -> 

	Given an array nums, find the length of the smallest subarray which has sum >= target
	
And now, the whole problem becomes a piece of cake, right?

Because now, all we need to do is keep adding the numbers as you iterate through the array and as soon as the sum so far becomes >= target then that means we found one possible solution. 

But we do not stop there. Since we found one possible solution, we now try to see if removing any elements from this solution/subarray also maintains the conditions that sum >= target. If yes, that means, we found a smaller subarray that fulfills the condition and so that will now be the new possible solution.

e.g. [2,3,1,2] will be a valid subarray as sum >= k
But now, we can see if we remove elements from the beginning, does that affect its validity? 

e.g. if we remove 2, then window becomes [3,1,2] 
Still the sum is >=k. This means, we found a subarray smaller than [2,3,1,2] which means this smaller subarray is a better candidate to be a solution.

And this is what we will do with each of the valid subarrays we find.

And this way, at the end, we will get the length of the smallest subarray with sum >= target


There might be cases when there is no subarray that has sum >= target. In that case, we can initialize the length to be infinity at the beginning. SO that if after doing the calculations, length is still infinity, that just means we did not find any subarray that satisfies the condition so we can return 0 in that case.
