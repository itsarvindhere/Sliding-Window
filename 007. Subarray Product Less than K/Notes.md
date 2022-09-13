# PROBLEM STATEMENT
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

1 <= nums[i] <= 1000

e.g. nums = [10,5,2,6], k = 100

There are 8 subarrays that have product less than 100:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

So output = 8

# IDENTIFICATION

The problem clearly says that we are given an array of positive numbers >= 1 and <= 1000

It also says we have to return number of subarrays

It also has a condition for each subarray

So this is clearly a case where we can use Variable Size Sliding Window.


# VARIABLE SIZE SLIDING WINDOW APPROACH

All we need to do is in each iteration, check if the product that we have got so far is <= k or not. If it is, that means it violates the condition which says the product needs to be "strictly" less than k i.e, product < k.

So, until product is not less than k, we can keep shrinking the current window/subarray.

And once that is done, we can be sure that the current window has product of all numbers < k

Now comes the interesting part. We want to keep the count of subarrays with product of numbers < k.

e.g. nums = [10,5,2,6], k = 100

WE know subarrays with product < 100 are -> [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]


In first iteration, product will be 10. Since it is already < k, we want to make count = 1 since [10] is a subarray in itself
In 2nd iteration, product will be 50. We want to make count = 2 since [10,5] is a subarray in itself
In 3rd iteration, it will be 100. Because 100 >= 100, now we want to shrink the window. We will remove 10 and product becomes (52 = 10)
So, count = 3 because [5,2] is also a valid subarray
In 4th iteration, product = 60. Again, count = 4 since [5,2,6] is also a subarray.
And loop ends with count = 4

But wait. What about the subarrays such as [5], [2], [6], [2,6] ??

```
The reason is that we are incrementing the count wrong. 
```

Lets start with [10]. Since it is valid, that means all the subarrays of it are also valid. Its subarray is only [10] => 1
Then we got [10,5]. Since it is valid, that means, all subarrays are also valid. Its subarrays are => [10], [5], [10,5]
But since we already got [10] earlier we won't consider that again. So, valid subarrays for [10,5] are [5] and [10,5] => 2

Next is [5,2]. For this, there are three subarrays => [5], [2], [5,2]. But since we already took care of [5] before, valid subarrays for [5,2] are [2], [5,2] => 2

Next we got [5,2,6]. For this, the subarrays are => [5], [2], [6], [5,2], [2,6], [5,2,6] Since we already took care of [5],  [2] and [5,2] earlier, we will only consider the other three i.e., [6], [2,6], [5,2,6] => 3

So in total we have 1 + 2 + 2 + 3 => 8 valid subarrays

```
In short, for a valid window, the valid subarray count = length of that window
This is the reason why we don't just do count++ 
Instead we do count += (j - i + 1) 
Where (j - i + 1) gives us the length of current window/subarray
```