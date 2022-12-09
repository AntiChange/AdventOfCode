import copy

def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def checkDistanceAndMove(headCoord, tailCoord):
    xDistance = headCoord[0] - tailCoord[0]
    yDistance = headCoord[1] - tailCoord[1]
    if (abs(xDistance) < 2 and abs(yDistance) < 2):
        # The rope will not break; do not move
        return [0, 0]
    elif (xDistance and yDistance):
        # The two points are on different rows and columns. Move diagonally
        return [xDistance // abs(xDistance), yDistance // abs(yDistance)]
    elif (xDistance):
        return [xDistance // abs(xDistance), 0]
    else:
        return [0, yDistance // abs(yDistance)]

def solution(input):
    snake = [[0, 0] for i in range(10)]
    visited = {}
    totalVisited = 0

    for commands in input:
        command = commands.split(" ")
        if (command[0] == "L"):
            for i in range(int(command[1])):
                snake[0][0] -= 1
                for j in range(9):
                    move = checkDistanceAndMove(snake[j], snake[j + 1])
                    snake[j + 1][0] += move[0] 
                    snake[j + 1][1] += move[1] 
                if tuple(snake[9]) not in visited.keys():
                    visited[tuple(snake[9])] = True
                    totalVisited += 1
        elif (command[0] == "R"):
            for i in range(int(command[1])):
                snake[0][0] += 1
                for j in range(9):
                    move = checkDistanceAndMove(snake[j], snake[j + 1])
                    snake[j + 1][0] += move[0] 
                    snake[j + 1][1] += move[1] 
                if tuple(snake[9]) not in visited.keys():
                    visited[tuple(snake[9])] = True
                    totalVisited += 1
        elif (command[0] == "U"):
            for i in range(int(command[1])):
                snake[0][1] += 1
                for j in range(9):
                    move = checkDistanceAndMove(snake[j], snake[j + 1])
                    snake[j + 1][0] += move[0] 
                    snake[j + 1][1] += move[1] 
                if tuple(snake[9]) not in visited.keys():
                    visited[tuple(snake[9])] = True
                    totalVisited += 1
        else:
            for i in range(int(command[1])):
                snake[0][1] -= 1
                for j in range(9):
                    move = checkDistanceAndMove(snake[j], snake[j + 1])
                    snake[j + 1][0] += move[0] 
                    snake[j + 1][1] += move[1] 
                if tuple(snake[9]) not in visited.keys():
                    visited[tuple(snake[9])] = True
                    totalVisited += 1
    
    return totalVisited

print(solution(parse("input.txt")))
