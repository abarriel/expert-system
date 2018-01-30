#!/usr/bin/python3
import sys
import re

def dict_gen(k):
    yield chr(k+65)
    yield { 'value': None }

class bc:
    BLUE = '\033[1;96m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    RED = '\033[1;91m'
    RES = '\033[0m'
    BOLD = '\033[1m'

if len(sys.argv) != 2:
    print(bc.RED, "Add a file in parameters", bc.RES)
    sys.exit(1)

reSpaceandCom = ["[\r\t\f\v ]|\#.*", ""]
reAvoidDuplicate = ["\n+", "\n"]

cleanFileAndReturnList = lambda file: re.sub(*(reAvoidDuplicate + [re.sub(*(reSpaceandCom + [file]))])).strip().split('\n')
filterByFirst = lambda file, char: list(filter(file, file[0] == char))
listToDict = lambda array, value: dict((v, value) for v in array)
filterFirstChar = lambda array, char: list([x for x in array if x[0] == char][0])

getGoals = lambda file: listToDict((filterFirstChar(file, '?')[1:]), False)
getFacts = lambda file: listToDict((filterFirstChar(file, '=')[1:]), True)

fileBrut = open(sys.argv[1], "r").read()
file = cleanFileAndReturnList(fileBrut)
goals = getGoals(file)
facts = getFacts(file)
rules = file[:-2]
dic = dict(map(dict_gen, range(26)))

if not goals:
    print(bc.RED, "no goals providen", bc.RES)
    sys.exit(1)

print(bc.GREEN + 'Facts:', facts, bc.RES, "\n")
print(bc.BLUE + 'Goals:', goals, bc.RES, "\n")
print(bc.YELLOW + 'Rules:\n\n' + "\n".join(rules), bc.RES, "\n")
