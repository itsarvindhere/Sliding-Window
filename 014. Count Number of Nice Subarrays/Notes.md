# PROBLEM STATEMENT

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given an array related problem
 -> We have to find number of subarrays
 -> We are given a condition to find a subarray


 So yes, this is a variable size sliding window related problem as this asks us to return number of subarrays and there is no fixed window count. 


# VARIABLE SIZE SLIDING WINDOW - APPROACH

There are some things to take care of in this problem. We cannot simply consider one window to be valid and just increment count by 1.

Consider this ->

		nums = [2,2,2,1,2,2,1,2,2,2] and k = 2
				0 1 2 3 4 5 6 7 8 9
		
So, if we use the sliding window approach, then we will start from index 0 and until the count of odd numbers does not become k, we will keep increasing window size. Now just by looking at the array you will see that when index is  6 then it will have two odd numbers from 0th index to 6th index.

So we will have a valid window with k odd numbers -

			[2,2,2,1,2,2,1]

But, at this moment, we cannot simply do count += 1. Just think about it. If [2,2,2,1,2,2,1] is a valid subarray with k odd numbers, then how many subarrays of this are also valid?

	These are all valid subarrays with k odd numbers
	[2,2,2,1,2,2,1]
	[2,2,1,2,2,1]
	[2,1,2,2,1]
	[1,2,2,1]
	
This means, we cannot do count += 1 only. We have to check for a particular nice subarray, how many total nice subarrays are possible.

And to find that, just see above what is the smallest possible subarray. It is [1,2,2,1]. Why we were not able to get more subarrays smaller than it? Because we would've lost one odd number and that would've violated the condition of k odd numbers.

So this means, just see how many numbers are there between the beginning of the window and the first odd number in the window i.e., the leftmost odd number.

Finally, we will get a general formula as 
	
		(index of leftmost odd number in current window - index of beginning of window) + 1
		
So basically, we want to keep track of not just the odd numbers but also their indices. 

And so we can use a queue here to keep all the indices in it from left to right as we encounter odd numbers so that to calculate the count, we can simply get the first item in the queue as that will always be the leftmost odd number index of current window.

And as we shrink the window, we will keep checking if the item we are removing from window is an odd number or not. If yes, that means we need to remove the leftmost item from queue as well. 

# ANOTHER WAY OF APPROACHING SUCH PROBLEMS - O(1) SPACE 

Just remember one thing for such problems where we have to find how many subarrays have "exactly" K something. 

	Subarrays with K something = Subarrays with at most K something - Subarrays with at most K-1 something
	
At most K means that a subarray should have something <= K. 
	
For this problem, since we have to find subarrays with exactly K odd numbers. That means, 
	
	Subarrays with exactly K odd numbers  = Subarrays with at most K odd numbers  - Subarrays with at most K-1 odd numbers
	
Let us prove it with an example.

		nums = [1,1,2,1,1], k = 3
		
So here, what are the subarrays with <= 3 odd number ? i.e., how many subarrays have at most 3 odd numbers?

	[1], [1, 1], [1], [1, 1, 2], [1, 2], [2], [1, 1, 2, 1], [1, 2, 1], [2, 1], [1], [1, 2, 1, 1], [2, 1, 1], [1, 1], [1] => 14 Subarrays

Now, lets see how many subarrays have <= 2 odd numbers i.e., <= K- 1 odd numbers
	
	[1], [1, 1], [1], [1, 1, 2], [1, 2], [2],  [1, 2, 1], [2, 1], [1], [2, 1, 1], [1, 1], [1] => 12 Subarrays
	
So that means, Subarrays with exactly 3 odd numbers are => 14 - 12 => 2

And to prove this, here are all the subarrays with exactly 3 odd numbers
	
		[1,1,2,1] and [1,2,1,1].
		
And these are the only ones that are not in the list of subarrays with <= 2 odd numbers. 

We can use this template in many similar problems where we are asked to find how many subarrays have exactly K sum, exactly K odd numbers and so on. And there is little to no change we have to make which makes this solution so damn useful.