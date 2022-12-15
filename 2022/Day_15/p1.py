def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip().split(" "))
    
    return inputlines

def solution(input):
    # ---------------- Initial attempt ----------------
    # Leads to memory error, as x/y values are extremely large. Also lots of 
    # complications with negative numbers (which are dealt with) but sacrifices too 
    # much memory.
    # Also note that when printed out, x and y are inverted.

    # xMax = 0
    # yMax = 0
    # for line in input:
    #     xMax = max(xMax, int(line[2][2:-1]), int(line[8][2:-1]))
    #     yMax = max(yMax, int(line[3][2:-1]), int(line[9][2:]))

    # # Worst case, board needs to be xMax + yMax (rows and col)
    # board = [(["."] * (3 * (xMax + yMax))) for i in range(3 * (xMax + yMax))] 

    # for line in input:
    #     # Adding (xMax + yMax) to account for negative values
    #     sensor = [int(line[2][2:-1]) + (xMax + yMax), int(line[3][2:-1]) + (xMax + yMax)]
    #     beacon = [int(line[8][2:-1]) + (xMax + yMax), int(line[9][2:]) + (xMax + yMax)]

    #     taxicabDist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    #     for i in range(-taxicabDist, taxicabDist + 1):
    #         y = taxicabDist - abs(i)
    #         for j in range(-y, y + 1):
    #             if (board[sensor[0] + i][sensor[1] + j] != "B"):
    #                 board[sensor[0] + i][sensor[1] + j] = "#"
    #     board[beacon[0]][beacon[1]] = "B"
        
    # total = 0
    # for row in board:
    #     if row[2000000 + (xMax + yMax)] == "#":
    #         total += 1

    # return total

    # ---------------- Solution ----------------
    # Don't need to recreate the board, since we only care about y = 2000000
    seen = {}
    for line in input:
        targetRow = 2000000
        
        # Coordinates in [x, y] (col, row)
        sensor = [int(line[2][2:-1]), int(line[3][2:-1])]
        beacon = [int(line[8][2:-1]), int(line[9][2:])]
        taxicabDist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        # Calculate how "wide" the influence ono the x axis is
        xDist = taxicabDist - abs(sensor[1] - targetRow)
        if (xDist >= 0):
            for i in range(-xDist, xDist + 1):
                if (sensor[0] + i not in seen.keys() or seen[sensor[0] + i] != "B"):
                    seen[sensor[0] + i] = "#"
        
        if (beacon[1] == targetRow):
            seen[beacon[0]] = "B"

    count = 0
    for val in seen.values():
        if val == "#":
            count += 1

    return count


print(solution(parse("input.txt")))
