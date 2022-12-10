def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    cycle = 0
    register = 1
    curLine = ""
    for commands in input:
        command = commands.split(" ")
        if (len(command) == 1):
            if (abs((cycle % 40) - register) <= 1):
                curLine += "#"
            else:
                curLine += "."
            cycle += 1
            if ((cycle % 40 == 0) and (cycle <= 240)):
                print(curLine)
                curLine = ""
        else:
            for i in range(2):
                if (abs((cycle % 40) - register) <= 1):
                    curLine += "#"
                else:
                    curLine += "."
                cycle += 1
                if ((cycle % 40 == 0) and (cycle <= 240)):
                    print(curLine)
                    curLine = ""
            register += int(command[1])

    return


print(solution(parse("input.txt")))
