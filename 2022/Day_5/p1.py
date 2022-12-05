def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines


def solution(input):
    numStacks = len(input[0]) // 4 # Each stack takes up 4 characters. (including newline)
    stacks = [[] for i in range(numStacks)]

    for line in input:
        if (line[0] == "["):
            for i in range(1, 4*numStacks, 4):
                if (line[i] != " "):
                    stacks[(i - 1) // 4].insert(0, line[i])
            
        elif (line[0] == "m"):
            command = line.split(" ")
            for i in range(int(command[1])):
                stacks[int(command[5]) - 1].append(stacks[int(command[3]) - 1].pop())                

    result = ""
    for stack in stacks:
        if (len(stack) != 0):
            result += stack[-1]
    
    return result


print(solution(parse("input.txt")))
