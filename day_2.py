# Set direction variables and start in middle of a 1-3 grid.
# Going up and left is negative, down and right is positive
ud = 3
lr = 1

# Define where each button is using a dictionary
# Coordinates are ud,lr
numberPad = {
    "1,3" : '1',
    "2,2" : '2',
    "2,3" : '3',
    "2,4" : '4',
    "3,1" : '5',
    "3,2" : '6',
    "3,3" : '7',
    "3,4" : '8',
    "3,5" : '9',
    "4,2" : 'A',
    "4,3" : 'B',
    "4,4" : 'C',
    "5,3" : 'D'
}

answer = ""


def findButton(row):
    global ud, lr, numberPad, answer
    for direction in row:
        # print(direction)
        if direction == "U":
            if str(ud - 1) + "," + str(lr) in numberPad:
                ud -= 1
        elif direction == "D":
            if str(ud + 1) + "," + str(lr) in numberPad:
                ud += 1
        elif direction == "L":
            if str(ud) + "," + str(lr - 1) in numberPad:
                lr -= 1
        elif direction == "R":
            if str(ud) + "," + str(lr + 1) in numberPad:
                lr += 1

        # print("%s,%s" % (ud, lr))
    coordinates = str(ud) + "," + str(lr)
    if coordinates in numberPad:
        print numberPad[coordinates]
        answer += str(numberPad[coordinates])
    else:
        print("Coordinates unbound!")


while True:
    instruction = raw_input("Please input instructions \n")
    if instruction != "end":
        findButton(instruction)
    else:
        print answer
        break
