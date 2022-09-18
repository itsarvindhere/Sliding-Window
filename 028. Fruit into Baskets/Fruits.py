def totalFruit(fruits):
    dict = {}
    maxFruits = 0
        
    i,j = 0,0
    n = len(fruits)
        
    while j < n:
        dict[fruits[j]] = 1 if not fruits[j] in dict else dict[fruits[j]] + 1
            
        # Length of Dictionary represents how many types of fruits are there in current window
        while len(dict) > 2:
            dict[fruits[i]] -= 1
            if dict[fruits[i]] == 0: dict.pop(fruits[i])
            i += 1
            
        # And when the above check is done, we can be sure that current window has at most 2 types of fruits only, not more than that
        maxFruits = max(maxFruits, j - i + 1)
            
        j += 1
        
    return maxFruits


fruits = [1,2,3,2,2]
maxFruitsWeCanPick = totalFruit(fruits)

print("Maximum Number of Fruits we can pick ->", maxFruitsWeCanPick)