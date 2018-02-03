import sys

def dict_gen(k):
    yield chr(k + 65)
    yield { 'value': None }

class bc:
    BLUE = '\033[1;96m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    RED = '\033[1;91m'
    RES = '\033[0m'
    BOLD = '\033[1m'

def error(str, line = ''):
    print(bc.RED, str, line, bc.RES)
    sys.exit(1)
class p:
    green = lambda st: print(bc.GREEN, st, bc.RES)
    blue = lambda st: print(bc.BLUE, st, bc.RES)
    red = lambda st: print(bc.RED, st, bc.RES)

def printdic(dic):
    for letter, key in dic.items():
        if key['value'] == True:
            p.green('\t\t{}: True'.format(letter))
        if key['value'] == None:
            print('{}: None'.format(letter))
        if key['value'] == False:
            p.red('\t{}: False'.format(letter))