
# Declare Direction Variable
# N = 1, E = 2, S = 3, W = 4
# We start facing North
facing = 1

# Declare longitude (N,S) and latitude (E,W) for keeping track of where we are
longitude = 0
latitude = 0

# List of coordinates visited
longLines = [];
latLines = [];

def moveCharacter(instruction):
    global facing
    global longitude
    global latitude

    direction = instruction[0]
    distance = int(instruction[1:len(instruction)])

    # Set what direction we are facing
    if direction == "L":
        facing -= 1
        if facing < 1: # If we move left past north, set to west
            facing = 4
    elif direction == "R":
        facing += 1
        if facing > 4: # If we move right past west, set to north
            facing = 1

    # Walk the distance
    # If moving north or east, add one. If going south or west, minus one
    if facing == 1:
        longStart = longitude
        longitude += distance
        longEnd = longitude
        longLines.append([longStart, longEnd])
    elif facing == 2:
        latStart = latitude
        latitude += distance
        latEnd = latitude
        latLines.append([latStart, latEnd])
    elif facing == 3:
        longStart = longitude
        longitude -= distance
        longEnd = longitude
        longLines.append([longStart, longEnd])
    elif facing == 4:
        longStart = longitude
        latitude -= distance
        latEnd = latitude
        latLines.append([latStart, latEnd])

    return

def checkVisited():


    return

while True:
    instruction = raw_input()
    if instruction == "end":
        totalDistance = abs(latitude) + abs(longitude)
        print (totalDistance)
        break;
    elif instruction == "string":
        instruction = raw_input("Enter list of instructions: \n")
        instructionList = instruction.split(", ")
        for move in instructionList:
            moveCharacter(move)
        #     if checkVisited(longitude, latitude):
        #         found = True;
        #         break;
        # found = True;

    else:
        moveCharacter(instruction)

    totalDistance = abs(latitude) + abs(longitude)
    print (totalDistance)
    break
