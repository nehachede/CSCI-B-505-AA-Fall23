def place_crystals(mushroom_heights):
    crystal_positions = []
    stack = []

    for i in range(0,len(mushroom_heights)):
        while stack and mushroom_heights[i] >= mushroom_heights[stack[-1]]:
            stack.pop()
        if not stack or i - stack[-1] > i:
            crystal_positions.append(i)
        stack.append(i)

    return crystal_positions

# Test cases
#print(place_crystals([3, 2, 5, 4, 1]))  # [0, 2]
# print(place_crystals([7, 1, 2, 3])) # [0]