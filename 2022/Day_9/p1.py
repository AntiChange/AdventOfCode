import copy

def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def checkDistance(headCoord, tailCoord):
    if (abs(headCoord[0] - tailCoord[0]) >= 2 or abs(headCoord[1] - tailCoord[1]) >= 2):
        return True
    return False

def solution(input):
    head, tail = [0, 0], [0, 0]
    visited = {}
    totalVisited = 0

    for commands in input:
        command = commands.split(" ")
        if (command[0] == "L"):
            for i in range(int(command[1])):
                prev = copy.deepcopy(head)
                head[0] -= 1
                if (checkDistance(head, tail)):
                    tail = prev
                if tuple(tail) not in visited.keys():
                    visited[tuple(tail)] = True
                    totalVisited += 1
        elif (command[0] == "R"):
            for i in range(int(command[1])):
                prev = copy.deepcopy(head)
                head[0] += 1
                if (checkDistance(head, tail)):
                    tail = prev
                if tuple(tail) not in visited.keys():
                    visited[tuple(tail)] = True
                    totalVisited += 1
        elif (command[0] == "U"):
            for i in range(int(command[1])):
                prev = copy.deepcopy(head)
                head[1] += 1
                if (checkDistance(head, tail)):
                    tail = prev
                if tuple(tail) not in visited.keys():
                    visited[tuple(tail)] = True
                    totalVisited += 1
        else:
            for i in range(int(command[1])):
                prev = copy.deepcopy(head)
                head[1] -= 1
                if (checkDistance(head, tail)):
                    tail = prev
                if tuple(tail) not in visited.keys():
                    visited[tuple(tail)] = True
                    totalVisited += 1
    
    return totalVisited


print(solution(parse("input.txt")))
