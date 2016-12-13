from collections import defaultdict
import operator

puzzleInput = open('puzzle.txt', 'r')

strings = defaultdict(str)
for line in puzzleInput:
    for i in range(0, len(line)): # for each letter in the line
        strings[i] += line[i]

columns = {}
columns = dict(strings)
message = ""
for index, column in columns.items():
    letterValues = {}
    for letter in column:
        number = column.count(letter)
        letterValues[letter] = number
    sort = sorted(letterValues.items(), key=operator.itemgetter(1))
    message += sort[0][0]

print (message)
