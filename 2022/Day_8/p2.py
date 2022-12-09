def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

# ---------------------INITIAL SOLUTION----------------------------
# Supposedly more efficient, but faulty. Unsure where the issue lies,
# saving for future reference. 

# def solution(input):
    
    # # We parse the input similarly to part 1, only use a running count
    # # of the longest view in each direction. We then use the tracker to 
    # # calculate total scenic scores
    
    # scenicTracker = [([1] * len(input[0])) for i in range(len(input))]

    # # Left->right direction
    # for r in range(len(input)):
    #     count = 0
    #     for c in range(len(input[0])):
    #         if (c == 0):
    #             scenicTracker[r][c] = 0
    #         elif (input[r][c - 1] > input[r][c]):
    #             count = 1
    #         elif (input[r][c - 1] == input[r][c]):
    #             count += 1
    #         else:
    #             count += 1
    #             scenicTracker[r][c] *= count

    # # right->left direction
    # for r in range(len(input)):
    #     count = 0
    #     for c in range(len(input[0]) - 1, -1, -1):
    #         if (c == (len(input[0]) - 1)):
    #             scenicTracker[r][c] = 0
    #         elif (input[r][c + 1] > input[r][c]):
    #             count = 1
    #         elif (input[r][c + 1] == input[r][c]):
    #             count += 1
    #         else:
    #             count += 1
    #             scenicTracker[r][c] *= count

    # # up->down direction
    # for c in range(len(input[0])):
    #     count = 0
    #     for r in range(len(input)):
    #         if (r == 0):
    #             scenicTracker[r][c] = 0
    #         elif (input[r - 1][c] > input[r][c]):
    #             count = 1
    #         elif (input[r - 1][c] == input[r][c]):
    #             count += 1            
    #         else:
    #             count += 1
    #             scenicTracker[r][c] *= count

    # # down->up direction
    # for c in range(len(input[0])):
    #     count = 0
    #     for r in range(len(input) - 1, -1, -1):
    #         if (r == (len(input) - 1)):
    #             scenicTracker[r][c] = 0
    #         elif (input[r + 1][c] > input[r][c]):
    #             count = 1
    #         elif (input[r + 1][c] == input[r][c]):
    #             count += 1
    #         else:
    #             count += 1
    #             scenicTracker[r][c] *= count

    # scenicMax = 0
    # for r in range(len(input)):
    #     for c in range(len(input[0])):
    #         scenicMax = max(scenicMax, scenicTracker[r][c])

    # return scenicMax

# ---------------------WORKING SOLUTION-------------------------
def solution(input):
    maxScenic = 0
    for r in range(1, len(input) - 1):
        for c in range(1, len(input[0]) - 1):
            curScore = 1

            count = 0
            # left direction
            for i in range(r - 1, -1, -1):
                count += 1
                if (input[i][c] >= input[r][c]):
                    break
            curScore *= count

            count = 0
            # right direction
            for j in range(r + 1, len(input)):
                count += 1
                if (input[j][c] >= input[r][c]):
                    break
            curScore *= count

            count = 0
            # up direction
            for k in range(c - 1, -1, -1):
                count += 1
                if (input[r][k] >= input[r][c]):
                    break
            curScore *= count

            count = 0
            # down direction
            for k in range(c + 1, len(input[0])):
                count += 1
                if (input[r][k] >= input[r][c]):
                    break
            curScore *= count

            maxScenic = max(curScore, maxScenic)

    return maxScenic

print(solution(parse("input.txt")))
