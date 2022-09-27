from sortedcontainers import SortedList
def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    list = SortedList()

    for i,num in enumerate(nums):
            
        # To get the correct index to put the current element
        idealIndex = SortedList.bisect_left(list, num)
            
        # From this index, we can retrieve the floor and ceil
        # Floor will simply be the ideal index of current element - 1
        floor,ceil = idealIndex - 1, idealIndex
            
        # If there is a largest value that is just smaller than current number
        # Check if their difference is <= valueDiff
        # If yes, then return True as we found a pair
        if floor >= 0 and floor < len(list):
            if num - list[floor] <= valueDiff: return True
            
        # If there is a smallest value that is just larger than current number
        # Check if their difference is <= valueDiff
        # If yes, then return True as we found a pair
        if ceil >= 0 and ceil < len(list):
            if list[ceil] - num <= valueDiff: return True

        list.add(num)

        if len(list) > indexDiff: list.remove(nums[i - indexDiff])
    
    return False


nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0  

print("Is there a valid pair? -> ", containsNearbyAlmostDuplicate(nums,indexDiff, valueDiff))