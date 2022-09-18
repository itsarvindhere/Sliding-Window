# PROBLEM STATEMENT

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 1. Given an array
 2. We have to return the smallest range
 3. Condition is given

But how is this a sliding window problem?


We want to get a range such that the range elements from all the lists.

What we will do is, take the given 2D array and flat it to a 1D array but, in that 1D array, each element will be a tuple with each tuple having the number as well as which list it belongs to i.e.g, index of list in 2D array.

Now, all that's left is to find a window with smallest range. The valid window should have index of all the lists appearing at least once.

ANd now, it sounds like a sliding window problem right?

# VARIABLE SIZE SLIDING WINDOW - APPROACH

Take the given list -> Flat it and convert it to a 1D array -> Make sure each 1D array element is a tuple with element as also the list number it belongs to

Then sort this array.

And now it becomes a problem of Sliding Window. 


		nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
		
		If we take each element and combine it with its list index and then flat out this nums array, we get
		
		flat_nums = [(4, 0), (10, 0), (15, 0), (24, 0), (26, 0), (0, 1), (9, 1), (12, 1), (20, 1), (5, 2), (18, 2), (22, 2), (30, 2)]
		
So, first value is the number itself and the second value is the index of list in the original array

Now sort this list because we want a range -> [smallest,largest]
After sorting - 

		sorted = [(0, 1), (4, 0), (5, 2), (9, 1), (10, 0), (12, 1), (15, 0), (18, 2), (20, 1), (22, 2), (24, 0), (26, 0), (30, 2)]

So now, all we need to do is find the minimum range by finding a window which has elements from all the K list types.

e.g. in above, we can have a window as [(0, 1), (4, 0), (5, 2)] because it has elements from all three lists i.e., 0, 1  and 2
In this case, range will be [0,5]

Similarly, we can have a window [(4, 0), (5, 2), (9, 1)] with range [4,9] and so on...

We can then use the mentioned formula in the problem to find the smaller range and update the range array.