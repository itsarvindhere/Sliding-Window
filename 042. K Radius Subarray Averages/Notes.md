# PROBLEM STATEMENT

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

# EXAMPLE

Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.


# FIXED SIZE SLIDING WINDOW - IDENTIFICATION AND APPROACH

  -> Given an array problem
  -> We are given k which is the radius
  -> This means a subarray needs to have a size = diameter
  -> We want to find the average for each subarray of size = diameter


  Since we are given the radius as input i.e., k

This means, a valid subarray should have size = diameter i.e., 2 * radius.

But since we are dealing with 0-based indexing, subarray size = (2 * radius) + 1

This means, we need to take each subarray of size = (2 * radius) + 1, find the average and then set the value of the center of this subarray as avg in the output array.

The center of a subarray that starts with i is simply (i + k)

		[7,4,3,9,1,8,5,2,6], k = 3
		
		So, we have to consider subarrays of size = 2 * 3 + 1 => 7
		
		First, we get the subarray [7,4,3,9,1,8,5]
		
		Now, for this one, average = sum of all numbers/k => 37
		
		What is the center of this subarray? i.e., the radius. Just by looking we can see the center is at index = 3 
		i.e., (starting index + k)
		
		So, in the output array, at index = (starting index + k ) put the value = avg