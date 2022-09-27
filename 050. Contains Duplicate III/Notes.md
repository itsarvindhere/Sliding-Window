# PROBLEM STATEMENT
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

    i != j,
    abs(i - j) <= indexDiff.
    abs(nums[i] - nums[j]) <= valueDiff

Return true if such pair exists or false otherwise.

# EXAMPLE

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

# APPROACH

In languages such as Java, we have built-in class such as a TreeSet that uses a self-balancing binary search tree. But in Python, there isn't such built in class. So, we can make use of SortedList which kinds of works the similar way as a self-balancing binary search tree.

So basically, what we want in this problem is a pair such that the distance between the indices is not more than indexDiff and the difference between the values is not more than valueDiff. 

The brute force solution is pretty straightforward as you just use two nested loops but that is going to fail for large test cases.

```
# BRUTE FORCE O(n^2) - TIME LIMIT EXCEEDED
class Solution:
     def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
         for i in range(0, len(nums)):
             for j in range(i + 1, i + indexDiff + 1):
                 if j < len(nums) and abs(nums[i] - nums[j]) <= valueDiff: return True
         return False
```

So can we do it in a more efficient way? Lets understand with the help of an example.


			nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
			
			So, we can pick any two indices, given that their difference is <= 3
			Since we have indices from 0 to 3 here,
			It simply means that we can pick any pair from this array. 
			But that pair should have value difference <= valueDiff
			
			e.g. if we take index 0 and 1, their difference = 1 <= indexDiff
			But difference of their values =  2 - 1 = 1 > valueDiff so not valid!
			
			This also means that the indexDiff specifies the size of a window from which can we pick indices.
			3 means any pair from a window size of 3 + 1 = 4 (since 0-based indexing) is valid 
			
Okay. So we got the idea that window size will be 4. But how to pick? We cannot just go through each and every combination as that again is a brute force approach.

Just think about it. We do not need to go through each and every pair in a window.

If I ask you if you are given a number and you have to find what numbers in the list will result in the minimum absolute difference between that given number then how will you do it? 

		e.g. [4,6,10] and number = 7
		
		Which number will result in the minimum absolute difference? 
		Ofcourse it will be 6 right? Because it is the nearest to the given number
		
		Take another example -> [1,3,8,10,13] number = 12
		This time it will be 13 because it is nearer to 12 than 10. 
		
In simple words, for any given number, its floor and ceil values in the array will result in the minimum absolute difference. And that's the whole point. We just want either floor or the ceil value for a number in the window of size indexDiff + 1 If any one of them give us a value difference <= valueDiff then we simply return True.

In case of Java's TreeSet, you get methods such as TreeSet.floor() and TreeSet.ceiling() which return you the floor and ceiling of a given number in the set. But in case of SortedList(), there are no such built in methods.

What we do have in a sortedList() are two methods named - bisect_left and bisect_right. 

What they do is -> for any number, return the index at which it should be inserted if we want to maintain a sorted order in the SortedList. 

"Left" and "Right" just mean in case the number we are inserting is already present, "bisect_left" will return the index to the left of that number and "bisect_right" will return index to the right of that number. Anywyas, you can read more about these SortedList methods here - https://grantjenks.com/docs/sortedcontainers/sortedlist.html

The Runtime complexity if approximately O(logn)

So, if we got a correct index for a number, we can then find the floor and ceiling of that number from that index easily. 

		e.g. if sortedList is [1,2,4] and number to insert is "3"
		Then bisect_left will give us the index = 2. Because that's the index at which 3 should come so that list remains sorted.
		And since we got index = 2, what is the floor of 3 in the array. It is 2. Which is at index = 1. 
		And ceil is 4 which is at index = 2
		
		In short, floor = whatever bisect_left returns - 1
		And ceil = whatever bisect_left returns
		
		
And all that's left now is to calculate the difference between floor and number or ceil and number, given that floor and ceil are valid indices in the list.  If difference is <= valueDiff, return True.

Otherwise, add that number in the list and move to the next iteration.

Also, since window size is indexDiff + 1, if the item we added is the last item in this window, then that means we now need to move to the next window. In other words, we need to remove the first element of this window now which is (index of last element of this window - indexDiff)