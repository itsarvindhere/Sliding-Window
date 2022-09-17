# PROBLEM STATMENT
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.

EXAMPLE:

    Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
    Output: 3
    Explanation: 
    It is possible to run all individual and consecutive pairs of robots within budget.
    To obtain answer 3, consider the first 3 robots. The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 which is less than 25.
    It can be shown that it is not possible to run more than 3 consecutive robots within budget, so we return 3.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

  -> We are given arrays
  -> We are asked to find a consecutive Robots count i.e, a subarray
  -> The condition for a subarray to be valid is also given

So yes, this is a variable size sliding window problem.


# VARIABLE SIZE SLIDING WINDOW - APPROACH

This problem is somewhat similar to the "Sliding Window Maximum" Problem.

That's because in this, the only extra step is to keep track of the runningCost as well. Also, in Sliding Window Maximum, we had the length of window given but here, we are not given the size of window which means it is a Variable Size Sliding Window problem.

Otherwise, we are doing the same thing here which is, we are using a deque to keep track of maximum element's index in current window so that if we move to nextwindow and for that window as well the same element is max, we are not recalculating the max. 

And at the same time, we are also tracking the runningCost using a variable 'sum'.

Then we check the condition - 

    Is max(window) + (length of window * sum) more than budget? 

If yes, then that means shrink this window by incrementing ith index i..e, move the window from left side but keep right side as it is. And also check if the previous ith index element is max or not. If it was max, also remove the index from beginning of deque. 
