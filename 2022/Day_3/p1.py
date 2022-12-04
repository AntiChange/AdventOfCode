def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    # Find the recurring 
    priorityTotal = 0
    for line in input:
        # Extract rucksack items
        halfway = (len(line) - 1) // 2
        firstHalf = line[0 : halfway] # Minus the newline character
        secondHalf = line[halfway : len(line) - 1]
        
        # Find duplicate item
        # Sort and use two pointers to find duplicate item for O(nlogn)
        firstHalf = sorted(firstHalf)
        secondHalf = sorted(secondHalf)
        p1, p2 = 0, 0
        while (True):
            if firstHalf[p1] == secondHalf[p2]:
                duplicateItem = ord(firstHalf[p1])
                if duplicateItem > 96:
                    # Duplicate item is lowercase. 'a' = 97 -> Subtract 96 so 'a' = 1
                    priorityTotal += duplicateItem - 96
                else:
                    # Duplicate item is uppercase. 'A' = 65 -> Subtract 38 so 'A' = 27
                    priorityTotal += duplicateItem - 38
                break
            elif (firstHalf[p1] > secondHalf[p2]):
                p2 += 1
            else:
                p1 += 1

    return priorityTotal


print(solution(parse("input.txt")))
