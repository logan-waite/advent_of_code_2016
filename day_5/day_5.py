import hashlib

def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def FindPassword(doorID):
    password = ["","","","","","","",""]
    filledIndices = []
    found = 0
    count = 0
    while found < 8:
        toHash = doorID + str(count)
        roomHash = hashlib.md5(toHash)
        hexValue = roomHash.hexdigest()
        goodHash = False

        if str(hexValue[:5]) == "00000":
            goodHash = True

        if goodHash and IsInt(hexValue[5]):
            if not int(hexValue[5]) > 7 and not hexValue[5] in filledIndices:
                index = int(hexValue[5])
                password[index] = hexValue[6]
                found += 1
                filledIndices.append(hexValue[5])
                print(password)


        count += 1
    final = ""
    for letter in password:
        final += letter
    return final

doorID = raw_input("Please enter the Door ID \n")

print(FindPassword(doorID))
