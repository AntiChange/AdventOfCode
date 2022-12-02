def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    calories = []
    current = 0
    
    for line in input:
        if (line == "\n"):
            calories.append(current)
            current = 0
        else:
            current += int(line)
        
    return sum(sorted(calories)[-3:])

print(solution(parse("input2.txt")))