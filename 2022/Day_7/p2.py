# We will represent this problem using a tree structure,
# where nodes represent directories or files, which store 
# the file size in the case of a file or the total contained
# file size in the case of a directory.

# We will also keep track of the previous/parent node for convenience.
class Node:
    def __init__(self, name, size=-1):
        self.name = name
        self.prev = None 
        self.size = size
        self.next = []
   

def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i)
    
    return inputlines

def determineSize(node):
    if (len(node.next) == 0):
        return node.size
    totalSize = 0
    for n in node.next:
        totalSize += determineSize(n)
    node.size = totalSize
    return totalSize
    
# For debugging
def printTree(node):
    print(node.name, node.size)
    if (node.prev):
        print(" prev is " + node.prev.name)
    for n in node.next:
        print("\t" + n.name)
    for n in node.next:
        printTree(n)

def parseTree(node, requiredSpace):
    if (len(node.next) == 0):
        return float('inf')
    possibleSizes = []
    for n in node.next:
        possibleSizes.append(parseTree(n, requiredSpace))
    if (node.size > requiredSpace):
        possibleSizes.append(node.size)
    return min(possibleSizes)


def solution(input):
    head = Node("/")
    cur = head
    for commands in input:
        command = commands.strip().split(" ")
        if (len(command) == 3):
            if (command[2] == "/"):
                cur = head
            elif (command[2] == ".."):
                cur = cur.prev
            else:
                for node in cur.next:
                    if node.name == command[2]:
                        cur = node
        elif (command[0] == "dir"):
            # Add new directory
            newDirect = Node(command[1])
            newDirect.prev = cur
            cur.next.append(newDirect)
        elif (command[0] == "$"):
            # We can ignore ls commands with the setup
            continue
        else:
            # Add file. No need to set prev since we cannot 
            # cd into file
            newFile = Node(command[1], int(command[0]))
            cur.next.append(newFile)
        
    determineSize(head)
    
    # For debug
    # printTree(head)
    
    return parseTree(head, head.size - 40000000) 


print(solution(parse("input.txt")))
