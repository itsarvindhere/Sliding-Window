# PROBLEM STATEMENT

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

    For i <= k < j:
    arr[k] > arr[k + 1] when k is odd, and
    arr[k] < arr[k + 1] when k is even.
    Or, for i <= k < j:
    arr[k] > arr[k + 1] when k is even, and
    arr[k] < arr[k + 1] when k is odd.


# EXAMPLE

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> Given a problem of array
    -> We want to return the length of longest subarray
    -> The condition for a valid subarray is also given

Yep, this is a Variable Size Sliding Window Problem.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

Suppose array is 

					[9,4,2,10,7,8,8,1,9]
					
We can have two types of valid turbulent subarrays - 

			a > b < c > d < e
			a < b > c < d > e
			
And ofcourse, a number in itself is always turbulent. That's why in code, the initial value for maxSize is 1. 

So, we want to see if there are subarrays of size > 1 or not. If yes, we want to find the largest of them. Since first number of an array is already turbulent in itself, we will start checking from the 2nd number (Unless array has only 1 number, in that case we return 1).

In above example, we start from 4. Is 4 > 9? NO. Is 4 < 9? YES. This means, the number that comes after 4 should be > 4. Because we are following this pattern here ->  a < b > c < d > e

So, for every number, we not only check its previous number but also its next number. In this way, we do not have to keep track of what was the previous comparison sign. 

So, for every number, there are two cases - 

		It is smaller than previous and smaller than next
							Or
		It is bigger than previous and bigger than next

And well, those are the conditions that we have to use. Forget the even and odd thing that the problem statement mentions. If any of the above two conditions are true, that means current number can be included in the current window.


# EDGE CASES

What about cases when all elements are same in the array. 

			[100,100, 100] 
			
Here initially, ith pointer will point to first 100 and jth pointer to second 100.

Now, if our code runs, since we are calculating window size as j - i + 1, it will set maxSize to 2 which is not true. 

This means, if the current number and previous number is the same, then we need to skip the previous number as that will never be included in the valid subarray since a valid subarray can never have same adjacent numbers (It can have duplicate numbers present in different indices).
 