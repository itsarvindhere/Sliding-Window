# PROBLEM STATEMENT

You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

 -> We are given an array related problem
 -> We have to find number of consecutive cards to pick which means that we need to find a minimum length subarray 
 -> The condition is that the subarray should have a pair of matching cards in it i.e., two cards of same value

# VARIABLE SIZE SLIDING WINDOW - APPROACH

We need a way to know if a particular card has already been visited before. And well, that is something a Set can do.

So at each iteration, we check if the curent card is already in the set. If yes, that means we have visited it before. So we have a matching pair and now we can calculate the minimum length of the subarray that has a matching pair of cards. 

We keep shrinking the current window from left side for that until there is no longer a matching pair. And in the same iteration we also keep finding the minimum length

