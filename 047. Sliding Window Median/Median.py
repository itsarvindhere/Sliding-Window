# >py -m pip install sortedcontainers
from sortedcontainers import SortedList
def medianSlidingWindow(nums, k):
    medians = []
        
    # Time Complexity to remove an element from SortedList = O(logk)
    # Time Complexity to add an element into a SortedList = O(logk)
    sortedList = SortedList()
        
    i,j = 0,0
        
    while j < len(nums):
		# Insert the current number in sortedList
		# It will automatically be placed at its correct place
        sortedList.add(nums[j])
            
		# If window size is not yet k, increment j
        if j - i + 1 < k: j += 1
		# If window size becomes j, calculate the median
        else:
			# If k is even, median is the average of two middle elements
            if k % 2 == 0: medians.append((sortedList[k//2 - 1] + sortedList[k//2]) / 2)
			# Otherwise median is the middle element
            else: medians.append(sortedList[k//2])
                    
            # Remove calculations for the ith element
            sortedList.remove(nums[i])
                
            # Slide the window
            i += 1
            j += 1


    return medians

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print("Median Array is ->", medianSlidingWindow(nums,k))