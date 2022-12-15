def parse(filename):
    inputlines = []
    
    with open(filename, 'r') as f:
        for i in f.readlines():
            inputlines.append(i.strip().split(" "))
    
    return inputlines

def getTaxicab(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def solution(input):
    # The beacon must be unique, so it must be exactly 1 unit from the "edge" formed by a sensor and beacon.
    # Otherwise we could move it one unit closer to such edge and it would not be unique. Thus, we check
    # 1 unit from the "edge" of each beacon

    # Keeps track of sensor position, nearest beacon distance
    sensors = {}

    # Store position of all sensors
    for line in input:
        sensor = [int(line[2][2:-1]), int(line[3][2:-1])]
        beacon = [int(line[8][2:-1]), int(line[9][2:])]
        taxicabDist = getTaxicab(sensor[0], sensor[1], beacon[0], beacon[1])
        sensors[tuple(sensor)] = taxicabDist

    # Check all units 1 away from "edge"
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    # Iterate through units 1 distance from edge
    for sen, dist in sensors.items():
        for i in range(-dist, dist + 1):
            for sign in [1, -1]:
                j = dist - abs(i)
                for dir in directions:
                    valid = True
                    x = (sen[0] + i + dir[0])
                    y = (sen[1] + j * sign + dir[1])
                    if (x < 0 or x > 4000000 or y < 0 or y > 4000000):
                        continue
                    
                    #  Check distance from sensors
                    for sensor, distance in sensors.items():
                        if getTaxicab(x, y, sensor[0], sensor[1]) <= distance:
                            valid = False
                    
                    # Guaranteed to be unique by problem statement
                    if (valid):
                        return (x * 4000000 + y)
                        
                
        
    return "Not found"


print(solution(parse("input.txt")))
