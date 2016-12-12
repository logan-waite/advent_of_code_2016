
# Declare Direction Variable
# N = 1, E = 2, S = 3, W = 4
# We start facing North
facing = 1

# Declare longitude (N,S) and latitude (E,W) for keeping track of where we are
longitude = 0
latitude = 0

# List of coordinates visited
# coordinates are listed with long first
coordinates = [[0,0]]

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
    for i in range(0, distance):
        if facing == 1:
            longitude += 1
        elif facing == 2:
            latitude += 1
        elif facing == 3:
            longitude -= 1
        elif facing == 4:
            latitude -= 1

        if checkVisited(longitude, latitude):
            return True;
        else:
            coordinates.append([longitude, latitude])

    return False;

def checkVisited(longitude, latitude):
    pair = [longitude, latitude]
    if pair in coordinates:
        return True
    return False

while True:
    found = False
    instruction = raw_input()
    if instruction == "end":
        totalDistance = abs(latitude) + abs(longitude)
        print (totalDistance)
        break;
    elif instruction == "string":
        instruction = raw_input("Enter list of instructions: \n")
        instructionList = instruction.split(", ")
        for move in instructionList:
            if moveCharacter(move):
                found = True
                break;
        if found:
            totalDistance = abs(latitude) + abs(longitude)
            print (totalDistance)
            break;
    else:
        moveCharacter(instruction)
