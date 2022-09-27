from sortedcontainers import SortedList
def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    list = SortedList()
        
    i,j = 0,0
        
    while j < len(nums):
        # To get the correct index to put the current element
        idealIndex = SortedList.bisect_left(list, nums[j])
            
        # From this index, we can retrieve the floor and ceil
        # Floor will simply be the ideal index of current element - 1
        floor,ceil = idealIndex - 1, idealIndex
            
        # If there is a largest value that is just smaller than current number
        # Check if their difference is <= valueDiff
        # If yes, then return True as we found a pair
        if floor >= 0 and floor < len(list):
            if nums[j] - list[floor] <= valueDiff: return True
            
        # If there is a smallest value that is just larger than current number
        # Check if their difference is <= valueDiff
        # If yes, then return True as we found a pair
        if ceil >= 0 and ceil < len(list):
            if list[ceil] - nums[j] <= valueDiff: return True
                
        # Add the current element in the list
        list.add(nums[j])
            
        # If window size is not yet indexDiff + 1
        if j - i + 1 < indexDiff + 1: j += 1
        # If window size is reached, remove the first element of current window before moving to the next window
        else:
            list.remove(nums[i])
            i += 1
            j += 1
    
    return False


nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0  

print("Is there a valid pair? -> ", containsNearbyAlmostDuplicate(nums,indexDiff, valueDiff))