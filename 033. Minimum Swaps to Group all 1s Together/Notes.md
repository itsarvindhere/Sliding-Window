# PROBLEM STATEMENT
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

# FIXED SIZE SLIDING WINDOW - IDENTIFICATION

How is this problem a fixed size sliding window problem?

Yes we have an array but there is no mention of size of window right? Well, that is something we have to figure out.

Look at the problem statement carefully. It says a swap means take an element at an index and replace it with any other element at any other index. In this problem, a Swap does not mean swapping two adjacent elements only. It means we can swap any two elements.

This is what gives us an idea that if we first take note of how many 1s are present in the given array, then we can check each window of size = number of 1s because in that way, we can see how many zeros there are in that window. And to make sure that window has all 1s together, we would need to swap those zeros with the 1s that are not present in this window.

In other words, the number of zeros in a window = number of swaps needed for a window to have all 1s together.

And so, the Size of a Window = Total Number of 1s in a window. And now, it becomes a fixed size sliding window problem.

# FIXED SIZE SLIDING WINDOW - APPROACH

Since the array is circular, to make sure a test case does not cause any issues, I simply took the given array and appended it to itself so that last element is adjacent to the first element. 

e.g. nums = [1,1,0,0,1]
So, after appending nums = [1,1,0,0,1 , 1,1,0,0,1]

Since the above array has 3 1s, that means for any window of size 3, the least number of zeros are the minimum number of swaps needed.
In the above array -> nums = [1,1,0,0,1 , 1,1,0,0,1]

	We will start with window [1,1,0] and it has one zero. So for now, minimumSwaps = 1
	Next we have [1,0,0] and it has two zeros. Since 2 > 1, minimumSwaps is not updated
	Next is [0,0,1]. Same as above
	Next is [0,1,1]. Number of zero is 1 so minimumSwaps remains 1 only
	Next is [1,1,1] Here number of zeros is 0, that means minimumSwaps can be updated to 0. 
	
	And so on..

At the end, we will see that minimumSwaps is 0 which means we need no swaps to group the three 1s together since they are already grouped together. This also means, that if number of zeros in a window of size = number of 1s are 0,then we can straight away return from there as the 1s are already grouped together.

Lets take another example - 

e.g. nums = [0,1,1,1,0,0,1,1,0]

After appending it becomes nums = [0,1,1,1,0,0,1,1,0   ,  0,1,1,1,0,0,1,1,0 ]

So now, we see that original array has 5 1s. This means, we will check each window of length 5 and see which one has the minimum number of zeros. Less the zeros,  more the ones in that window or less swaps needed. That's the whole idea.
	
	We start with window [0,1,1,1,0]. Number of zeros = 2 so minimumSwaps = 2
	Then we have [1,1,1,0,0]. Number of zeros = 2 so minimumSwaps = 2
	Then we have [1,1,0,0,1]. Number of zeros = 2 so minimumSwaps = 2
	Then we have [1,0,0,1,1]. Number of zeros = 2 so minimumSwaps = 2
	Then we have [0,0,1,1,0]. Number of zeros = 3 and since 3 > 2, so minimumSwaps remains 2
	Then we have [0,1,1,0,0] Number of zeros = 3 and since 3 > 2, so minimumSwaps remains 2
	
	And so on...

	At the end, minimumSwaps will be 2 so we need only 2 swaps to make sure all 1s are together