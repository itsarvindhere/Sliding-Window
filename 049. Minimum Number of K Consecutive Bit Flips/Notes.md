# PROBLEM STATEMENT
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

# EXAMPLE

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

# APPROACH USING A QUEUE

We only flips a window if it starts with a 0 because we want the whole array to have only 1s. So we are not concered with 1s here. The main motive is to convert all 0 to 1 (If it is possible).

The brute force way is to check each window and then for each window, if it starts with 0, take each element and flip it. But ofcourse that is not efficient way because we will do repeatitive work.

	e.g. suppose nums = [0,1,0,1,0,1] and k = 3
	So it we take the first 3 length subarray we get [0,1,0]

	And since it starts with 0, we flip each element to get [1,0,1] and so array becomes 
			[1,0,1,1,0,1]
			
	Now when we go to next subarray of size 3, we get [0,1,1]
	And again for the same reason, we flip it to get [1,0,0] and array becomes 
			
			[1,1,0,0,0,1]
			
But did you notice that we flipped the second number in original array twice which resulted in it becoming the same as it was in the beginning. So first we flipped 1 to 0 and then we flipped 0 to 1. Eventually, we got the same number back. So our flipping is of no use for some cases.

In Simple words -

		Flipping 1 or 0 Even Number of times will give us the same number
		Flipping 1 or 0 Odd Number of times will give us the opposite
		
And since we want to convert all 0 to 1 and do not want to convert 1 to 0, we can say 

	  If a number is 0, flip it once if it has already been flipped even number of times
	  If a number is 1, flip is once if it has already been flipped odd number of times
	  
Because in both cases, we will get back 1. Which is our main motive here.

And now the main thing is to have a way to check if a current index has been flipped before? If yes, then how many times - Even number of times or Odd number of times.

And that's where Queue comes into the picture.  We will use the queue to keep track of all the k-length windows that have been flipped. And as we complete traversing a k length window, we will also remove it from queue as we no longer need to keep track of it.

The reason why we have to keep track is because of the same reason I explained above where we were flipping a 1 twice, just to get back 1 which was of no use. 

			e.g. [0,0,0,1,0,1,1,0], k = 3
			
If we take a subarray of size k, we get [0,0,0]
Because it starts with a 0 we can flip it. But we also need to check if it has already been flipped even number of times or not. Because only then we know it was 0 and again it became 0 after even flips. Since currently queue is empty or length is 0, it basically means even flips because 0 % 2 == 0 So we can flip this window.
	
And to track the flips for this window, we will also put the last index of this window in a queue. The last index is 2 i.e., (i + k - 1)
	
		nums =  [0,0,0,1,0,1,1,0]
		queue = [2]
		flips = 1

So now you can see that this queue basically tells how many times any element till index = 2 has been flipped. Since length of queue is 1, that means each element was flipped once. 

		Next window of size = 3 is [0,0,1] from index 1 to 3
	
Here, as it starts with a 0, we check is the length of queue even i.e., has this 0 been flipped even times? NO! Length of queue is 1 that means, this 0 has been flipped once so we do not need to flip it again as one flip has already turned it into a 1.

		Next window of size 3 = [0,1,0] from index 2 to 4
		
Again, it starts from a 0. And for the same reason as above, we do nothing as length of queue is odd so this 0 has been flipped odd times so it is already 1. 

And now, we move to index = 3 which means we are done with the window from index 0 to 2 of length 3. So we no longer need to track it in the queue and so, we remove the last index of previous window from the queue.

		nums =  [0,0,0,1,0,1,1,0]
		queue = []
		flips = 1

	We are now at index = 3 and the window of size k is [1,0,1]

We see that at index = 3, we have 1. We know that we will flip a 1 only if it has been flipped odd number of times because only in that case this 1 would've converted to 0. Here, length of queue = 0 which is even. So no need to flip. 

Do note that we only add the index of last window element if we flip this window. Here we did not flip the window [1,0,1] from index = 3 to 5

	Next window is [0,1,1] from index = 4 to 6

We see that at index = 4, we have 0. We check if this window has been flipped even times before. We see that length of queue == 0 which is even. So yes, we have to flip this window to convert this 0 to 1. And so, we also add the last index of this window in the queue to keep track of flips.
		
		nums =  [0,0,0,1,0,1,1,0]
		queue = [6]
		flips = 2

Next window is [1,1,0] from index = 5 to 7

Since the first element is 1, we check the length of queue. Length is 1, which is odd. So it means, this 1 has been flipped odd number of times before which means it should be 0 right now (if we had manually flipped). So to turn it back to 1, it needs to be flipped one more time. Hence, we flip this window and so, we also put the last index of this window in the queue.
		
		nums =  [0,0,0,1,0,1,1,0]
		queue = [6,7]
		flips = 3
		
Next, we reach the index = 6. And we see that at index = 6, we have 1. Since length of queue is even, it means that this 1 has not changed to 0 after all the previous flips. So we do not flip it.

But since we are done with index 6, we can safely remove it from queue.

		nums =  [0,0,0,1,0,1,1,0]
		queue = [7]
		flips = 3
		
And finally, we are at index = 7. We have 0. Since queue is of odd length now, it means 0 has been flipped odd times and so it has become 1. So no need to flip. And as we are done with index = 7, we can remove it from queue.

		nums =  [0,0,0,1,0,1,1,0]
		queue = []
		flips = 3
		
And loop ends and we see that since queue is empty, that means, we did 3 k-bit flips to convert all elements to 1.

# **WHEN CAN WE NOT CONVERT ALL 0 TO 1?**
The above example was for a valid array in which we can do 3 k-bit flips to turn all 0 to 1. What about invalid cases. How to check those?

	Lets take - nums = [1,1,0], k = 2
	q = []
	
We start with first index. As it is 1 and length of q is even, that means we don't need to flip it.
We come to the index = 1. Here again, we have 1 and length of q is even. So no flips.
Then we come to index = 2. Here we have 0. Since length of queue is even, that means we need to flip it. And also we store the last index of this window in the queue i.e., i + k - 1 => 2 + 2 - 1 => 3

So, 
	
	nums = [1,1,0], k = 2
	flips = 1
	q = [3]
	
But now our loop ends. And our queue is not empty. This means No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

It the array was [1,1,0,0] then we would be able to flip the last two zeros to 1 and in that case, queue would be empty.

In simple words - 

		If queue is empty, we can do some or 0 k-bit flips to get all 1s in the array
		If queue is not empty, there is no way to get all 1s by doing k-bit flips
