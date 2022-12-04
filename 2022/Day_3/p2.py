def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    totalPriority = 0
    for i in range(0, len(input), 3):
        items = []
        for j in range(3):
            items.append(input[i + j].strip()),

        # Find common element in all 3 rucksacks (O(n) runtime, O(n) memory where n is the 
        # total number of items)
        dicts = [{} for k in range(3)]

        for l in range(3):
            for item in items[l]:
                dicts[l][item] = True

        for item in dicts[0].keys():
            if item in dicts[1].keys() and item in dicts[2].keys():
                if ord(item) > 96:
                    # Duplicate item is lowercase. 'a' = 97 -> Subtract 96 so 'a' = 1
                    totalPriority += ord(item) - 96
                else:
                    # Duplicate item is uppercase. 'A' = 65 -> Subtract 38 so 'A' = 27
                    totalPriority += ord(item) - 38
                break

    return totalPriority


print(solution(parse("input.txt")))
