Let's say we are given an array

        2 3 4 2 9 7 1

And we are also given a number = 3 which is the size of subarray

We are asked to find the maximum sum in a 3-sized subarray in the above array.

So, if we take subarrays of size 3 from above array, we get - 

    2 3 4 -> Sum = 9
    3 4 2 -> Sum = 9
    4 2 9 -> Sum = 15
    2 9 7 -> Sum = 18
    9 7 1 -> Sum = 17

So, the maximum sum subarray of size 3 is [2,9,7]

# BRUTE FORCE APPROACH

The Brute force approach is use two nested loops.

    for i in range(0, len(arr))
        for j in range(i, i + k)
            sum += ....

In this approach, we will first take array [2,3,4] and take its sum and store the sum

Then in next iteration, we take array [3,4,2] take its sum and if sum is bigger than previous, change sum to current sum.

and so on...

# REPETITIVE WORK

Did you notice something we are doign again in each step?

Initially, we got [2,3,4] subarray and we sum it to get 9

Next, we got [3,4,5] subarray. And here again we are doing sum of each element. But that is not required because in the previous step itself, we have sum of 3 + 4

So this means, for each new subarray, we just need to add one element extra to the previous sum and remove the first element of previous subarray.

i.e., [2,3,4] -> 2 + 3 + 4     -> 9
      [3,4,5] ->     3 + 4 + 5 -> 9

So it means, to get sum of [3,4,5] we can do

            9 + 5 - 2

i.e., take previous SUM, add next element (5), remove the first element of previous subarray(2)


This means, we can improve the Brute Force solution by using a Window of size K each time we want to find sum.

Such that for next subarray, we just slide the window by one to the right such taht one element is added at end and one is removed from the start.


# HOW TO IDENTIFY PROBLEMS THAT CAN BE SOLVED USING SLIDING WINDOW

For Sliding Window related Problems, we will normally be given an Array or a String in the problem.

And because window is continuous this means the sliding window problems will mention "Subarray" or "Substring". 

And the problem will mention "largest" or "smallest" etc.

And finally, the problem may also have "K" i.e., size of window.

If all these are given, we can try to approach the problem using sliding window.


# TYPES OF SLIDING WINDOW

1. Fixed Sized Window -> we will be given a fixed size of subarray or substring in the problem


2. Variable Sized Window -> It is not explicitly mentioned what is the size of the window/subarray/substring. In fact, we are asked to return the window size. 

 e.g. We might be asked to return the largest subarray that has the sum = 3 

 So in case of variable sized window, we are given some condition and we have to find the largest or smallest subarray that satisfied that condition. SO, we do not know the size of subarray or substring beforehand
