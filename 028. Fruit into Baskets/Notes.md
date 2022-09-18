# PROBLEM STATEMENT

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.

    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.

    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.


Given the integer array fruits, return the maximum number of fruits you can pick.

# EXAMPLE

        fruits = [1,2,1]

Since we can only pick at most two types of fruits, that means we can consider this whole array since it is valid. So, we can pick from all the 3 trees in this case.


        fruits = [0,1,2,2]

Here, we have three types of fruits - 0, 1 and 2. So, we can either pick 0 and 1 or 1 and 2

So the valid subarrays are -> [0,1], [1,2] and [1,2,2]

Out of these, the largest subarray is [1,2,2] which means we can pick from 3 trees. Hence, return 3.


# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

How is this a sliding window problem?

Here is how - 

    -> We are given a fruits array
    -> We can pick from trees in left to right manner only i.e., subarrays
    -> And while picking, we make sure we pick at most two types of fruits only. i.e., we can either pick single type of fruit only or two types of fruits only but never more than that.
    -> This means, we want a longest subarray with at most 2 distinct types of fruits

And well, now it becomes a Variable Size Sliding Window Problem.

# VARIABLE SIZE SLIDING WINDOW - APPROACH

The approach is similar to how we find a longest subarray/substring with at most K distinct elemets/charactgers
