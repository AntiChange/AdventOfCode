def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    # ---------Initial solution---------

    # totalOverlaps = 0
    # for line in input:
    #     ranges = []
    #     for item in line.strip().split(","):
    #         ranges.append([int(i) for i in item.split("-")])
    #     if (ranges[0][0] <= ranges[1][1] and ranges[0][1] >= ranges[1][0]):
    #         totalOverlaps += 1

    # return totalOverlaps

    # ---------Simplified/Improved solution---------
    totalOverlaps = 0
    for line in input:
        ranges = []
        for item in line.strip().split(","):
            ranges.append([int(i) for i in item.split("-")])
        if (min(ranges[0][1], ranges[1][1]) - max(ranges[0][0], ranges[1][0]) >= 0):
            totalOverlaps += 1

    return totalOverlaps

print(solution(parse("input.txt")))
