def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def solution(input):
    curMonkey = -1
    
    # Dictionary keeps track of the test value, and which monkey to throw to if true/false
    throwCheck = {}

    # Dictionary keeps track of what monkeys are holding
    monkeyList = {}

    # Dictionary keeps track of operation performed by each monkey
    operatorList = {}

    for line in input:
        if not line:
            continue
        elif line[0] == "M":
            curMonkey += 1
        elif line[0] == "S":
            items = [int(x.rstrip(",")) for x in line.split(" ")[2:]]
            monkeyList[curMonkey] = items
        elif line[0] == "O":
            operators = line.split(" ")[3:]
            operatorList[curMonkey] = operators
        elif line[0] == "T":
            testNumber = int(line.split(" ")[3])
            throwCheck[curMonkey] = [testNumber]
        elif line[3] == "t":
            throwNumber = int(line.split(" ")[5])
            throwCheck[curMonkey].append(throwNumber)
        elif line[3] == "f":
            throwNumber = int(line.split(" ")[5])
            throwCheck[curMonkey].append(throwNumber)
        else:
            print("Something has gone terribly wrong.")
            print(line)
    
    # Keep track of how many times items were inspected
    inspectCheck = [0] * (curMonkey + 1)
    
    for round in range(20):
        for i in range(curMonkey + 1):
            while monkeyList[i]:
                inspectCheck[i] += 1
                item = monkeyList[i][0]
                val1 = item if (operatorList[i][0] == "old") else int(operatorList[i][0])
                val2 = item if (operatorList[i][2] == "old") else int(operatorList[i][2])
                item = (val1 * val2) if (operatorList[i][1] == "*") else (val1 + val2)
                item //= 3
                if (item % throwCheck[i][0] == 0):
                    monkeyList[throwCheck[i][1]].append(item)
                    monkeyList[i].pop(0)
                else:
                    monkeyList[throwCheck[i][2]].append(item)
                    monkeyList[i].pop(0)


    inspectCheck = sorted(inspectCheck)
    return inspectCheck[-1] * inspectCheck[-2]


print(solution(parse("input.txt")))
