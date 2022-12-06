from collections import defaultdict


def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    # Same as p1, but with 14 instead of 4
    input = input[0]
    window = defaultdict(int)
    for i in range(14):
        window[input[i]] += 1

    for i in range(14, len(input)):
        if (window[input[i - 14]] == 1):
            window.pop(input[i - 14])
        else:
            window[input[i - 14]] -= 1
        
        window[input[i]] += 1

        if (len(window) == 14):
            return i + 1        # Need to add one for 1-indexed
    
    return -1


print(solution(parse("input.txt")))
