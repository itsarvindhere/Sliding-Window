#Method to find how many subarrays have at most k distinct integers
def atMost(nums,k):

        # To keep the count of each integers in a window
        dict = {}

        # To Keep track of distinct integers in a window
        distincts = 0
        
        i,j = 0,0
        n = len(nums)
        count = 0
        
        while j < n:
            # Put the current integer in dictionary
            dict[nums[j]] = 1 if not nums[j] in dict else dict[nums[j]] + 1

            # If its count is 1, that means we got a new distinct integer
            if dict[nums[j]] == 1: distincts += 1
            
            #If the number of distinct integers in this window exceed k, then shrink the window from left until distincts is no longer > k
            if distincts > k:
                while distincts > k:
                    dict[nums[i]] -= 1
                    # If the integer removed results in its count becoming 0, that means one distinct integer has been removed from the window
                    if dict[nums[i]] == 0: distincts -= 1
                    i += 1
            count += j - i + 1
            j += 1
        
        return count
        
    
# Subarrays with K Distinct Integers = Subarrays with at most K distinct integers - Subarrays with at most K-1 distinct integers 
def subarraysWithKDistinct(nums, k):
    return atMost(nums,k) - atMost(nums,k-1)


nums = [1,2,1,2,3]
k = 2

count = subarraysWithKDistinct(nums,k)
print("Number of subarrays with exactly K distinct Integers ->", count)