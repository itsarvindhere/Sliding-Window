# PROBLEM STATMENT

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 

You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

In other words, whichever element is the max element in each window, return that. 

e.g. Input: nums = [1,3,-1,-3,5,3,6,7], k = 3

Here, the windows and their max elements are ->

    [1,3,-1]  -> 3
    [3,-1,-3] -> 3
    [-1,-3,5] -> 5
    [-3,5,3] -> 5
    [5,3,6] -> 6
    [3,6,7] -> 7

So, output is -> [3,3,5,5,6,7] 


Since it is explicitly mentioned that we have a sliding window, there is no doubt that it has to be solved using Sliding Window Approach.

# SLIDING WINDOW APPROACH

What is our objective here? We want to find the maximum in each window of size k.

And we also want it to be efficient. So we don't want that for a new window, we again go through each element in window to see which is max.

e.g.    nums = [1,3,-1,-3,5,3,6,7], k = 3

First window is [1,3,-1] and we know that here, max is 3. and other two are smaller than it.

Now, next window is [3,-1,-3] So now, instead of again comparing 3 with -1, which we have done before, we just need to compare it with the new element that we just got in new window i.e., -3. And if this new element is not bigger that means, for this new window as well, the max element is the same as previous window.

This means, we need to keep track of the maximum.

# WHAT IF WE TRY TO KEEP TRACK OF MAX ELEMENT IN EACH WINDOW?

Will this work? Lets see.

nums = [1,3,-1,-3,5,3,6,7], k = 3

So, i and j are both 0. So we have a max variable that keeps track of maximum in current window. Initially, max = first element = 1

Now, since window size is not yet k, we increment j. In next iteration, jth element is 3. Because 3 > max, max = 3. Window size is 2

Since window size not yet k, increment j. Now, jth element is -1. Because -1 is not > max, max remains 3. 

And now, the size of the window has become 3. It means, we can now put the max element for this window in output array. So we push 3 in output array.

We now want to slide the window i.e., increment i and j. Before incrementing i, we see if ith element is max element or not. Since it is not, we do nothing.

So, now, j points to index 3 i.e., element = -3. Since - 3 is not > 3 max remains 3. 

Again, we push 3 into output.

But here comes the interesting part. Because now we are going to slide the window and i will be incremented. Since ith element = max. What to do now? We have to remove this max now but what is the new max? How to keep track of that? 

This means, a single value variable will not be sufficient to keep track of maximum.


# USING A DEQUE TO KEEP TRACK OF MAXIMUM ELEMENTS IN A WINDOW

A Deque allows insertion and deletion from both ends - left and right. We can use this data structure to keep all those values that "might" be useful in next windows. So, we not only keep the maximum but also the values after the maximum value because if the maximum value is to be removed when we slide the window, then when we remove that value from deque, then we have all the values after that maximum value in the window. 

e.g. [3,2,1,5] k = 3

i = 0, j = 0, deque is empty.

At jth index, we have 3. Since deque is empty, just push it in deque. deque right now is [3]

Since window size is not 3 yet, increment j. At j = 1 index we have 2. Here, 2 is not bigger than 3 but, 2 might be useful in the future windows. So for this reason, we will put 2 in the deque. THIS IS IMPORTANT! We will put all the numbers in the deque that may be useful in future windows. 

dequeue becomes [3,2]

Again, j is incremented. At j = 1, we have 1. For same reason as above, push 1 to deque. Deque becomes [3,2,1]

And because we now found the window of length = k, For this window, the maximum is the first element in deque = 3. So push 3 in the output array.

Now comes the interesting part. 

We are going to slide this window which means i will be incremented to 1. But at i = 0, we have the max element of current window. So, that means, if this window is going to slide, this max element is also going to be removed from deque. And that's why, if nums[i] == deque[0] before sliding the window, then remove deque[0] i.e., dequeue.popleft()

So, deque is not [2,1], i is 1, j is 3

At j, we have 5. Because 5 is bigger than all the elements in deque, it means we no longer need any element in the deque since 5 is bigger than all. Remember above when we said we only keep the useful numbers. Here, as we got a number bigger than all the numbers in deque, then the numbers in deque are of no use now.


So, before pushing 5 to the deque, remove all the numbers that are smaller than 5 from the deque. 

        Deque now becomes [5]

And since window size is k, we take this first element of deque and push it into output array.

And since j is not length of array. We break out of loop.


So, for nums = [3,2,1,5] and k = 3, output is [3,5]


