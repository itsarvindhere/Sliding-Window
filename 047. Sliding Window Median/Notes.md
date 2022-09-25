# PROBLEM STATEMENT

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.


# EXAMPLE
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]


# FIXED SIZE SLIDING WINDOW APPROACH

We are given the window size already so all that we need to think about is how to efficiently find the median of each window. We want to avoid doing repeatitive work.

In python, there is a SortedContainers library that provides a SortedList class. This can be used here because SortedList does addition or removal of any element in logn time. Also, as the name says, it stores the elements in sorted order.

So in each iteration, keep adding the jth element in sorted list until the window size is not k. As soon as it is k, find the median and before sliding the window, remove the ith element from sortedlist. 

