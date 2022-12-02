def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    maximum = 0
    current = 0

    for line in input:
        if (line == "\n"):
            maximum = max(maximum, current)
            current = 0     
        else:
            current += int(line)

    return maximum


print(solution(parse("input1.txt")))
