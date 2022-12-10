def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    cycle = 0
    register = 1
    total = 0
    for commands in input:
        command = commands.split(" ")
        if (len(command) == 1):
            cycle += 1
            if (((cycle - 20) % 40 == 0) and (cycle <= 220)):
                total += cycle * register
        else:
            for i in range(2):
                cycle += 1
                if (((cycle - 20) % 40 == 0) and (cycle <= 220)):
                    total += cycle * register
            register += int(command[1])

    return total


print(solution(parse("input.txt")))
