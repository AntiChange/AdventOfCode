def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    return ""


print(solution(parse("input.txt")))
