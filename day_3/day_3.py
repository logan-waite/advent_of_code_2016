validTriangles = 0
count = 0
triangleSet = 0
triangle1 = []
triangle2 = []
triangle3 = []
triangles = [triangle1, triangle2, triangle3]

def checkTriangle(values):
    # Declare Variables
    global validTriangles, count, triangleSet
    global triangle1, triangle2, triangle3

    count += 1
    numbers = []

    # Get the numbers of the row separated
    sides = values.split()
    for side in sides:
        numbers.append(int(side))

    triangle1.append(numbers[0])
    triangle2.append(numbers[1])
    triangle3.append(numbers[2])
    triangleSet += 1

    # If we don't have enough to make a valid triangle:
    if triangleSet == 3:
        for triangle in triangles:
            triangle.sort(key=int)
            print(triangle)
            if (triangle[0] + triangle[1]) > triangle[2]:
                validTriangles += 1
            del triangle[:]
        triangleSet = 0



while True:
    instruction = raw_input("Please input instructions \n")

    if instruction != "end":
        checkTriangle(instruction)
    else:
        print(validTriangles)
        print("count: %s" % count)
        break
