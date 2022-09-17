# PROBLEM STATEMENT

There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 

# FIXED SIZE SLIDING WINDOW - IDENTIFICATION

At first glance, it does not look like a sliding window problem but it is all about understanding the problem statement.

Here is what is going on.

	1. There is a bookstore owner that is grumpy on some minutes and whenever he is grumpy customers will be unsatisfied
	2. Whenever he is grumpy, grumpy[i] will be 1 so the number of customers that will be unsatisfied at that time will be customers[i] 
	3. The owner has a trick to not be grumpy for "minutes" consecutive minutes. Understand this part. Each index in grumpy array specifies a minute
	4. This means, we can find a particular window of length = minutes such that if the owner uses his trick to not be grumpy during this whole window, then he can make sure maximum number of customers are satisfied which were not satisfied earlier

So, we have to do these things -

	1. First get hold of how many customers are satisfied already because at the end, we have to return the total number of customers satisfied  
	2. And now as mentioned above, find that particular window of length = minutes which has the highest number of unsatisfied customers. This way, we can be sure that when we use the trick to not be grumpy in this whole window, maximum number of customers will be satisfied.

So this means, the 2nd part is something we need to do using sliding window approach. Because in this, we have to pick a subarray of length = minutes which has maximum number of unsatisfied customers.


# FIXED SIZE SLIDING WINDOW - APPROACH

EXAMPLE: 
		  customers = [1,0,1,2,1,1,7,5]
		  grumpy = [0,1,0,1,0,1,0,1]
		  minutes = 3

Whenever, grumpy[i] is 0, that means customers[i] number of customers are satisfied already.

	So from above example -> Already Satisfied Customers = 10
	
Now, in [1,0,1,2,1,1,7,5], find the window of size 3 with maximum unsatisfied customers. At any index, customers are unsatisfied if at the same index, grumpy array has 1

	So, we will get the window [1,7,5] as the window with maximum unsatisfied customers.
	Here, 1 + 5 = 6 customers are unsatisfied
	
And now we use our technique to not be grumpy for this entire window. That means this whole window will not include satisfied customers. 

	So that means, the 6 customers which were not satisfied earlier in this window are now satisfied too 
	so we can add 6 to our already satisfied count

This means - 
	
	Max Satisfied Customers = Already Satisfied Customers + Customers Satisfied after using technique
	Max Satisfied Customers = 10 + 6 => 16
