import json

def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip())
    
    return inputlines


# ---------------Wrong solution--------------- 
# Did not account for the fact that nested lists can completely determine
# whether or not packets are in order; and thus we must use three states.

# def compare(left, right):
#     for i in range(len(left)):
#         if i == len(right):
#             # Right has ran out of elements
#             return False
#         if (isinstance(left[i], int) and isinstance(right[i], int)):
#             if (left[i] == right[i]):
#                 continue
#             return (left[i] < right[i])
#         elif (isinstance(left[i], list) and isinstance(right[i], list)):
#             if (compare(left[i], right[i]) == False):
#                 return False
#         elif (isinstance(left[i], list) and isinstance(right[i], int)):
#             if (compare(left[i], [right[i]]) == False):
#                 return False
#         elif (isinstance(right[i], list) and isinstance(left[i], int)):
#             if (compare([left[i]], right[i]) == False):
#                 return False
#         else:
#             print("something has gone terribly wrong")
#
#     return True

#---------------Final solution---------------
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
    # We are counting exact same pairs as indeterminate.
    return len(left) != len(right)

def solution(input):
    index = 1
    totalSum = 0
    packets = []
    for line in input:
        if line:
            packets.append(json.loads(line))
        else:
            # Left = packets[0], right = packets[1]
            if (compare(packets[0], packets[1]) == 1):
                totalSum += index
            packets = []
            index += 1
    
    return totalSum


print(solution(parse("input.txt")))
