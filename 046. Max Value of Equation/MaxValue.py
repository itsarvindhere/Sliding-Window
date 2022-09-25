from collections import deque
def findMaxValueOfEquation(points, k):
    # Since we want to find the max value of equation, initialize it with the minimum possible value i.e., negative infinity
        
    maxEqValue = float('-inf')

    # Keep track of maximum yi-xi
    queue = deque()

    # currentPoint = j
    j = 0
        
    while j < len(points):
        xj = points[j][0]
        yj = points[j][1]

        # Remove all values for which |xi - xj| is not <= k
        # Note that in queue we are storing a tuple as -> (yi-xi, xi)
        # Since the first value in queue is the maximum value for yi-xi so far
        # To get xi, we need the 2nd value in tuple i.e., queue[0][1]
            
        while queue and (xj - queue[0][1] > k): queue.popleft()
            
        # If queue is not empty that means we have a maximum value for yi-xi 
        # So just calculate the value of equation => (yj + xj) + (yi - xi)
        # (yi-xi) => first value in a tuple in the queue
            
        if queue: maxEqValue = max(maxEqValue, yj + xj + queue[0][0])
                
        # Before appending, remove all smaller values for (yi-xi) from queue 
        # because they will never be useful if there exists a value bigger than them
        while queue and queue[-1][0] < yj - xj : queue.pop()
            
        # Now append the yj-xj value for current point
        queue.append((yj - xj, xj))  
        j += 1

    return maxEqValue


points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1


print("Max Value of Equation is -> ", findMaxValueOfEquation(points,k))