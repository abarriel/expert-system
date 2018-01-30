#!/usr/bin/python3
import sys
import re

if len(sys.argv) != 2:
    print("Add a file in parameters")
    sys.exit(1)

reSpaceandCom = ["[\r\t\f\v ]|\#.*", ""]
reAvoidDuplicate = ["\n+", "\n"]

cleanFileAndReturnList = lambda file: re.sub(*(reAvoidDuplicate + [re.sub(*(reSpaceandCom + [file]))])).strip().split('\n')
filterByFirst = lambda file, char: list(filter(file, file[0] == char))
listToDict = lambda array, value: dict((v, value) for v in array)
filterFirstChar = lambda array, char: list([x for x in array if x[0] == char][0])

getGoals = lambda file: listToDict((filterFirstChar(file, '?')[1:]), False)
getRules = lambda file: listToDict((filterFirstChar(file, '=')[1:]), True)

fileBrut = open(sys.argv[1], "r").read()
file = cleanFileAndReturnList(fileBrut)
goals = getGoals(file)
rules =  getRules(file)

print(goals)
print(rules)