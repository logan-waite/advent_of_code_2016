import re
abba = re.compile(r"([a-z])([a-z])\2\1")
badAbba = re.compile(r"([a-z])\1{3}")
insideBrackets = re.compile(r"(?:\[[a-z]*)(([a-z])([a-z])\3\2)(?:[a-z]*\])")

puzzleInput = open('puzzle.txt', 'r')

supported = 0
notSupported = 0
count = 0
badABBA = 0
inside = 0
abbaMatch = 0
good = 0

for line in puzzleInput:
    count += 1

    if badAbba.search(line):
        badABBA += 1
    if insideBrackets.search(line):
        inside += 1
    if abba.search(line):
        abbaMatch += 1
    if not badAbba.search(line) and not insideBrackets.search(line):
        good += 1
        print(line)
        if abba.search(line):
            supported += 1
        else:
            notSupported += 1
    else:
        notSupported += 1

print("badABBA %s" % badABBA)
print("inside brackets %s" % inside)
print("abbaMatch %s" % abbaMatch)
print("good %s" % good)
print("supported %s " % supported)
print("not supported %s" % notSupported)
print("count: %s" % count)
