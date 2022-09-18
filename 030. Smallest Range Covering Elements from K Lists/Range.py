from cgitb import small


def smallestRange(nums):
    #Initialize the range with maximum values
    range = [-100000, 100000]
    k = len(nums)
        
    # Flat the given 2D array into a 1D array and also sort it
    # The Flat array will have tuples with each tuple having the item and also a number indicating which list it belongs to
    list = sorted([(item,i) for i,sublist in enumerate(nums) for item in sublist])
    i,j = 0,0
    n = len(list)
    dict = {}
    groups = 0
        
    while j < n:
        # Get the list number the jth tuple belongs to
        group = list[j][1]
            
        # Add it to the dictionary
        dict[group] = dict.get(group, 0) + 1
            
        # If this is the first time we are putting it into dictionary, increment groups
        if(dict[group] == 1): groups += 1
                
                
        # While the number of groups are the same as number of lists initially in the array, then do the calculations of finding range
        while groups == k:
            # a and b are the first and last elements of current window/range
            a = list[i][0]
            b = list[j][0]
                
            # c and d are the elements from previous range 
            c = range[0]
            d = range[1]

            # Check the condition and if true, update the range
            if((b  - a) < (d - c)):
                range[0] = a
                range[1] = b
            
            #Remove calculations for ith index before shrinking the window from left side
            dict[list[i][1]] -= 1
            if dict[list[i][1]] == 0: groups -= 1
                
            # Shrink the window from left side
            i += 1
        #Increase window size from right side
        j += 1

        
    return range

nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
range = smallestRange(nums)

print("Smallest Range Covering Elements from all lists ->", range)