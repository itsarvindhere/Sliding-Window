from collections import deque
def maximumRobots(chargeTimes, runningCosts, budget):
    maxRobots = 0
    
    # To efficiently track maximum element in a window
    queue = deque()
        
    i,j = 0,0
    sum = 0
    n = len(chargeTimes)
        
    while j < n:
        # if the element that we are going to add is bigger than the elements in queue, remove those smaller elements from queue first (from the end)
        while len(queue) > 0 and chargeTimes[j] > chargeTimes[queue[-1]]: queue.pop()  
                
        # And then insert the element that is bigger
        queue.append(j)
            
        # Also keep track of the running cost
        sum += runningCosts[j]
            
        # Now check the condition if total running cost exceeds the budget, that means shrink the window by incrementing ith index
        while len(queue) > 0 and chargeTimes[queue[0]] + ((j - i + 1) * sum) > budget:
            # If the ith index has maximum element of current window, then also remove that index from queue
            if i == queue[0]: queue.popleft()
            sum -= runningCosts[i]
            i += 1
            
        # If we are here, that means condition is met so we can safely update maxRobots with the maximum of the two values
        maxRobots = max(maxRobots, j - i + 1)
        j += 1
        
    return maxRobots


chargeTimes = [3,6,1,3,4]
runningCosts = [2,1,3,4,5]
budget = 25

maxRobots = maximumRobots(chargeTimes, runningCosts, budget)

print("Maximum Number of Consecutive Robots we can run under the given budget -> ", maxRobots)