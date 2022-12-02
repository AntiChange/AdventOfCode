def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    score = 0
    for line in input:
        oppChoice = ord(line[0]) - 64
        playerChoice = ord(line[2]) - 87 # ASCII minus 24 converts XYZ -> ABC, minus 63 corresponds to point bonus
        score += playerChoice # ASCII minus 64 corresponds to point bonus
        if (playerChoice == oppChoice):
            score += 3
        elif (playerChoice == 1):
            if (oppChoice == 3):
                score += 6
        elif (playerChoice == 2):
            if (oppChoice == 1):
                score += 6
        else:
            if (oppChoice == 2):
                score += 6
    
    return score


print(solution(parse("input1.txt")))
