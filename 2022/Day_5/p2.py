def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines


def solution(input):
    numStacks = len(input[0]) // 4
    stacks = [[] for i in range(numStacks)]

    for line in input:
        if (line[0] == "["):
            for i in range(1, 4*numStacks, 4):
                if (line[i] != " "):
                    stacks[(i - 1) // 4].insert(0, line[i])
        
        elif (line[0] == "m"):
            command = line.split(" ")
            for j in stacks[int(command[3]) - 1][-int(command[1]):]:    # Use list slicing
                stacks[int(command[5]) - 1].append(j)
            del stacks[int(command[3]) - 1][-int(command[1]):]
    
    result = ""
    for stack in stacks:
        if (len(stack) != 0):
            result += stack[-1]
    
    return result


print(solution(parse("input.txt")))
