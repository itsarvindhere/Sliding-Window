def maxSatisfied(customers, grumpy, minutes):
    #First find how many customers are already satisfied
    satisfied = 0
        
    for i,c in enumerate(customers): 
        if(grumpy[i] == 0): satisfied += c
                        
        
    # Now find out what is the maximum count of unsatisfied customers in a window of length = minutes
    # We just need to take that window and use the technique to not be grumpy for that whole window
    maxUnsatisfiedCustomers = 0
    unsatisfiedCount = 0
    start  = -1
        
    i,j = 0,0
        
    while j < len(customers):
        if grumpy[j] == 1: unsatisfiedCount += customers[j]
        if j - i + 1 < minutes: j += 1
        else:
            if unsatisfiedCount > maxUnsatisfiedCustomers:
                maxUnsatisfiedCustomers = unsatisfiedCount
                start = i
            if grumpy[i] == 1: unsatisfiedCount -= customers[i]
            i += 1
            j += 1
                
        
    # Now from the window we got, just take all the unsatisfied customers and add it to satisfied count 
    # because we have used our power to not be grumpy during this whole window
    while minutes > 0 and start < len(customers):
        if grumpy[start] == 1: satisfied += customers[start]
        start += 1
        minutes -= 1
        
                    
    return satisfied


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

count = maxSatisfied(customers, grumpy, minutes)
print("Maximum Satisfied Customers ->", count)