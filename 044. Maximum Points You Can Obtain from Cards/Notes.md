# PROBLEM STATEMENT

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


# EXAMPLE

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.


# FIXED SIZE SLIDING WINDOW - IDENTIFICATION AND APPROACH

We want to find the maximum sum of k cards we can get

		Sum of K cards = Total Sum of array - Sum of left out cards
		
		If we picked K cards, what are number of left out cards? 
		
		There are (length - k) cards that we did not pick
		
So, if we can find (length-k) cards with the least sum, then that means, the K cards left out will have the maximum sum. 
		
Hence, this problem can be divided into two parts now - 

	1. Find the minimum sum subarray of length = (length of array - k)
	2. Return (totalSum - minimumSum)