# PROBLEM STATEMENT

A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

    Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

# VARIABLE SIZE SLIDING WINDOW - IDENTIFICATION

    -> We are given a problem related to string
    -> We have to find the maximum length substring
    -> We are given a condition for a valid substring

So yes, this is a problem that can be solved using a Variable Size Sliding Window Approach

# VARIABLE SIZE SLIDING WINDOW - APPROACH\

The problem statement has the solution itself. If we read the problem statement clearly, we have two choices -

    (1). Either replace k number of "F" with "T"
    (2). Or replace k number of "T" with "F"

If we do (1), Then we need to see what is the maximum number of consecutive "T" in the string

If we do (2), Then we need to see what is the maximum number of consecutive "F" in the string

And we need to return the maximum length out of the two results.

So, this problem can be divided into two parts -

    1. Find the maximum length substring which has at most K number of "F"
    2. Find the maximum length substring which has at most K number of "T"

And after doing both, we need to return the maximum solution out of both.

