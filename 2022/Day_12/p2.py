def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    board = [[] for i in range(len(input))]
    start = []
    for row in range(len(input)):
        for col in range(len(input[0])):
            input[row].replace("S", "a")
            board[row].append(ord(input[row][col]))
            if (input[row][col] == "E"):
                start = [row, col, 0, 123]
    
    directions = ([0, 1], [1, 0], [0, -1], [-1, 0])

    # Queue elements store 4 elements [row, col, depth, previous]
    queue = [start]
    visited = [start[:2]]

    # Perform BFS, only from E to a this time.
    while (queue):
        cur = queue.pop(0)
        for dir in directions:
            newRow = cur[0] + dir[0]
            newCol = cur[1] + dir[1]
            if (newRow >= 0 and newRow < len(input) and newCol >= 0 and newCol < len(input[0])):
                if (board[newRow][newCol] == 97 and cur[3] == 98):
                    return cur[2] + 1 
                elif ((cur[3] - 1) <= board[newRow][newCol] and [newRow, newCol] not in visited):
                    queue.append([newRow, newCol, cur[2] + 1, board[newRow][newCol]])
                    visited.append([newRow, newCol])
                
    return "Not found"

print(solution(parse("input.txt")))
