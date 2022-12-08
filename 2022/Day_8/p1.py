def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    # We will consider each direction separately, determining
    # which trees are visible and keeping a running count.
    
    visibleCount = 0
    # Necessary to prevent re-counts of trees. Accessed in [row][column]
    # (row ascends as we move down the grid)
    addedTracker = [([0] * len(input[0])) for i in range(len(input))]

    # Left->right direction
    for r in range(len(input)):
        curMax = -1
        for c in range(len(input[0])):
            if (int(input[r][c]) > curMax and addedTracker[r][c] == 0):
                visibleCount += 1
                addedTracker[r][c] = 1
            curMax = max(curMax, int(input[r][c]))
    
    # right->left direction
    for r in range(len(input)):
        curMax = -1
        for c in range(len(input[0]) - 1, -1, -1):
            if (int(input[r][c]) > curMax and addedTracker[r][c] == 0):
                visibleCount += 1
                addedTracker[r][c] = 1
            curMax = max(curMax, int(input[r][c]))
    
    # up->down direction
    for c in range(len(input[0])):
        curMax = -1
        for r in range(len(input)):
            if (int(input[r][c]) > curMax and addedTracker[r][c] == 0):
                visibleCount += 1
                addedTracker[r][c] = 1
            curMax = max(curMax, int(input[r][c]))   

    # down->up direction
    for c in range(len(input[0])):
        curMax = -1
        for r in range(len(input) - 1, -1, -1):
            if (int(input[r][c]) > curMax and addedTracker[r][c] == 0):
                visibleCount += 1
                addedTracker[r][c] = 1
            curMax = max(curMax, int(input[r][c]))      

    return visibleCount


print(solution(parse("input.txt")))
