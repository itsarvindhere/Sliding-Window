def subarraySum(nums,k):
        
        count = 0
        dict = {}

        prefixSum = 0
        
        for num in nums:   
            prefixSum += num
            
            if(prefixSum == k): count += 1
                
            if(prefixSum - k in dict): count += dict[prefixSum - k]
                
            dict[prefixSum] = 1 if prefixSum not in dict else dict[prefixSum] + 1
    
        
        return count

nums = [10,-5,15,15,-10,5] 
k = 5

count = subarraySum(nums,k)

print("Number of Subarrays with Sum K -> ", count)