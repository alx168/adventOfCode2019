def parseData():
    f = open("input.txt")
    wire1 = f.readline().strip().split(",")
    wire2 = f.readline().strip().split(",")
    return wire1, wire2

def buildCoords(wire):
    coords = [(0,0)]
    for step in wire:
        direction = step[0]
        magnitude = int(step[1:])
        prevX,prevY = coords[-1]
         
        if direction == "R":
            for i in range(1, magnitude + 1):
                coords.append((prevX + i, prevY)) 
        elif direction == "L":
            for i in range(1, magnitude + 1):
                coords.append((prevX - i, prevY)) 
        elif direction == "U":
            for i in range(1, magnitude + 1):
                coords.append((prevX, prevY + i)) 
        else:
            for i in range(1, magnitude + 1):
                coords.append((prevX, prevY - i)) 
    return coords

def manDist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def part1():
    wire1, wire2 = parseData()
    coords1 = buildCoords(wire1)
    coords2 = buildCoords(wire2) 
    
    intersectPoints = set(coords1).intersection(set(coords2)).difference({(0,0)})
    minDist = float("inf")
    for point in intersectPoints:
        minDist = min(minDist, manDist((0,0), point)) 
    return minDist

def pathLen(coords, p1):
    return coords.index(p1)  

def part2():
    wire1, wire2 = parseData()
    coords1 = buildCoords(wire1)
    coords2 = buildCoords(wire2) 
    
    intersectPoints = set(coords1).intersection(set(coords2)).difference({(0,0)})
    
    minLen = float("inf")
    for p in intersectPoints: 
        totalLen = pathLen(coords1, p) + pathLen(coords2, p)
        minLen = min(minLen, totalLen)
    return minLen
        
print(part2())
