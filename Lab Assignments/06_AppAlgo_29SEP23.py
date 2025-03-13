def max_treasure(treasure_houses, current_house):
    
    if current_house >= len(treasure_houses):
        return 0
    
    rob = treasure_houses[current_house] + max_treasure(treasure_houses, current_house + 2)
    skip = max_treasure(treasure_houses, current_house + 1)
        
    return max(rob, skip)

# print(max_treasure([20, 12, 15, 30, 16], 1))