def minimumCardPickup(cards):
    # Set to track if a card has already been visited
    s = set()
        
    maxValue = len(cards) + 1
    minCount = maxValue
        
        
    i,j = 0,0
        
    while j < len(cards):
        # If the card at index j is already in set that means we found a matching pair
        # So we can shrink the window until the element is still in set and also find the minimum length in each iteration
        if cards[j] in s:
            while cards[j] in s:
                minCount = min(minCount, j - i + 1)
                if cards[i] in s: s.discard(cards[i])
                i += 1
            
        # At this point, we are sure that card at index j is not in set so we can safely put it in set
        s.add(cards[j])
        j += 1
        
    return minCount if minCount != maxValue else -1

cards = [3,4,2,3,4,7]
minimumCards = minimumCardPickup(cards)

print("Minimum number of consecutive cards you have to pick up to have a pair of matching cards ->", minimumCards)