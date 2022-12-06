from collections import defaultdict


def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def solution(input):
    # Sliding window using dictionary
    input = input[0]
    window = defaultdict(int)
    for i in range(4):
        window[input[i]] += 1
    print(window)

    for i in range(4, len(input)):
        if (window[input[i - 4]] == 1):
            window.pop(input[i - 4])
        else:
            window[input[i - 4]] -= 1
        
        window[input[i]] += 1

        if (len(window) == 4):
            return i + 1        # Need to add one for 1-indexed
    
    return -1


print(solution(parse("input.txt")))
