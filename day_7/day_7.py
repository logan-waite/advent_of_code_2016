import re
abbaRe = re.compile(r"([a-z])([a-z])\2\1")
badAbba = re.compile(r"([a-z])\1{3}")
insideBrackets = re.compile(r"(?:\[[a-z]*)(([a-z])([a-z])\3\2)(?:[a-z]*\])")

r"\[[a-z]*(([a-z])([a-z])\3\2)[a-z]*\]"
r"\[[a-z]*(([a-z])([a-z])\3\2)[a-z]*\]"

r"([a-z])\1{3}"
r"([a-z])\1{3}"
puzzleInput = open('puzzle.txt', 'r')
supported = 0

for line in puzzleInput:

    if badAbba.search(line):
        matchString = badAbba.search(line)
        line = badAbba.sub(",", line)

    if abbaRe.search(line):
        abbaString = abbaRe.search(line)
        if not insideBrackets.search(line):
            supported += 1

print("supported %s " % supported)
