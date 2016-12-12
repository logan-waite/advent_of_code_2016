import re
import operator

pattern = re.compile("([a-z\-]+)-(\d+)\[([a-z]+)\]")
roomTotal = 0
f = open("roomList.txt", "w")

def separateID(info):
    if pattern.match(info):
        match = pattern.match(info)
        return match
    else:
        return False

def checkRoom(roomData):
    global pattern, roomTotal

    match = separateID(roomData)

    if match is not False:
        nameWithDashes = match.group(1)
        sectorID = match.group(2)
        checksum = match.group(3)

        name = nameWithDashes.replace("-", "")
        letters = {}

        for letter in name:
            number = name.count(letter)
            letters[letter] = number


        sort1 = sorted(letters.items(), key=operator.itemgetter(0))
        sort2 = sorted(sort1, key=operator.itemgetter(1), reverse=True)

        top5Letters = []
        for i in range(0,5):
            top5Letters.append(sort2[i][0])

        joiner = ""
        check = joiner.join(top5Letters)

        if check == checksum:
            roomTotal += int(sectorID)
            return True

    return False

def decodeRoom(roomID):
    global f

    match = separateID(roomID)
    name = match.group(1)
    sectorID = match.group(2)
    print(name)
    print(sectorID)

    decipheredName = ""
    for letter in name:
        if letter is not "-":
            newLetter = ord(letter)
            for i in range(0, int(sectorID)):
                newLetter += 1
                if newLetter == 123:
                    newLetter = 97
            decipheredName += chr(newLetter)
        else:
            decipheredName += letter

    f.write(decipheredName + " " + sectorID + "\n")
    # print(decipheredName + " " + sectorID)

while True:
    instruction = raw_input()

    if instruction != "end":
        if checkRoom(instruction):
            decodeRoom(instruction)
    else:
        print(roomTotal)
        # print("count: %s" % count)
        break
