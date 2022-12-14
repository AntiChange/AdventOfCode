def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    # iterate once to find maxes necessary to create (initial) board
    maxRow = 0
    maxCol = 0
    for line in input:
        pairList = [x.strip().split(",") for x in line.split("->")]
        for pair in pairList:
            maxRow = max(maxRow, int(pair[1]))
            maxCol = max(maxCol, int(pair[0]))
    
    # For extra row before new wall
    maxRow += 1

    # Add 1 to maxRow/maxCol for 1-indexed. Multiplied column by 2 to account for worst case
    board = [(["."] * (maxCol * 2)) for i in range(maxRow + 1)]
    
    # Generate paths in board
    # Note pairs are in order [col, row]
    for line in input:
        pairList = [x.strip().split(",") for x in line.split("->")]
        prevPair = pairList[0]
        for i in range(1, len(pairList)):
            if pairList[i][0] == prevPair[0]:
                for j in range(min(int(pairList[i][1]), int(prevPair[1])), max(int(pairList[i][1]), int(prevPair[1])) + 1):
                    board[j][int(prevPair[0])] = "#"
            else:
                for j in range(min(int(pairList[i][0]), int(prevPair[0])), max(int(pairList[i][0]), int(prevPair[0])) + 1):
                    board[int(prevPair[1])][j] = "#"
            prevPair = pairList[i]

    restCount = 0
    sandPos = [0, 500]

    while (True):
        # Necessary duplicate code to prevent accessing out of range index
        if (sandPos[0] == maxRow):
            restCount += 1
            board[sandPos[0]][sandPos[1]] = "o"
            sandPos = [0, 500]
        elif (board[sandPos[0] + 1][sandPos[1]] == "."):
            sandPos[0] += 1
        elif (board[sandPos[0] + 1][sandPos[1] - 1] == "."):
            sandPos[0] += 1
            sandPos[1] -= 1
        elif (board[sandPos[0] + 1][sandPos[1] + 1] == "."):
            sandPos[0] += 1
            sandPos[1] += 1
        else:
            restCount += 1
            # Now forced to this exit condition
            if (sandPos == [0, 500]):
                break
            board[sandPos[0]][sandPos[1]] = "o"
            sandPos = [0, 500]

    return restCount


print(solution(parse("input.txt")))
