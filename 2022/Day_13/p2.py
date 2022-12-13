from functools import cmp_to_key
import json

def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines

def compare(left, right):
    if (isinstance(left, int) and isinstance(right, int)):
        if (left < right):
            return 1
        elif (left == right):
            return 0
        else:
            return -1
    if (isinstance(left, int)):
        left = [left]
    elif (isinstance(right, int)):
        right = [right]
    for i in range(len(left)):
        if i == len(right):
            return -1
        result = compare(left[i], right[i])
        if (result != 0):
            return result
    return len(left) != len(right)


def solution(input):
    totalProduct = 1
    packets = []
    for line in input:
        if line:
            packets.append(json.loads(line))
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(compare), reverse=True)

    for i in range(len(packets)):
        if packets[i] == [[6]] or packets[i] == [[2]]:
            totalProduct *= (i + 1)

    return totalProduct


print(solution(parse("input.txt")))
