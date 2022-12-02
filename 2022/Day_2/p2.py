def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    score = 0
    for line in input:
        oppChoice = line[0]
        matchReq = line[2]
        if (matchReq == "X"):
            if (oppChoice == "A"):
                score += 3
            else:
                score += ord(oppChoice) - 65
        elif (matchReq == "Y"):
            score += (3 + ord(oppChoice) - 64)
        else:
            if (oppChoice == "C"):
                score += 7
            else:
                score += (6 + ord(oppChoice) - 63)
    
    return score

print(solution(parse("input2.txt")))
