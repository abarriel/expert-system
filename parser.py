#!/usr/bin/python3
import sys, re, argparse
from tools import bc, dict_gen, error

reSpaceandCom = ["[\r\t\f\v ]|\#.*", ""]
reAvoidDuplicate = ["\n+", "\n"]

cleanFileAndReturnList = lambda file: re.sub(*(reAvoidDuplicate + [re.sub(*(reSpaceandCom + [file]))])).strip().split('\n')
filterByFirst = lambda file, char: list(filter(file, file[0] == char))
listToDict = lambda array, value: dict((v, value) for v in array)
filterFirstChar = lambda array, char: list([x for x in array if x[0] == char][0])

divideRule = lambda rule, operator: list(re.match(r"(.*)" + re.escape(operator) + r"(.*)", rule).groups())
getGoals = lambda file: listToDict((filterFirstChar(file, '?')[1:]), False)
getFacts = lambda file: listToDict((filterFirstChar(file, '=')[1:]), True)

def setdic(dic, facts, val=True):
    for letter in dic:
        for fact in facts:
            dic[fact]['value'] = val

def parseArg(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument("-v", "--verbose", help="verbosity", action="store_true")
    parser.add_argument("-d", "--default", help="Set uninitialized to False", action="store_false", default=None)
    return parser.parse_args()

def bracket(rule, res = 0) :
    for (idx, c) in enumerate(rule):
        if c == '(':
            res += 1
        if c == ')':
            res -= 1
            if res < 0:
                return -1
        return bracket(rule[(idx + 1)::], res)
    return res

def parseFile(file, default):
    try:
        fileBrut = open(file, "r").read()
    except:
        error("Failed to read file")
    try:
        file = cleanFileAndReturnList(fileBrut)
        goals = getGoals(file)
        facts = getFacts(file)
        rules = file[:-2]
        dic = {}
        # dic = dict(map(lambda k: dict_gen(k, default), range(26)))
    except:
        error("Failed to parse file")
    if not goals:
        error("No Goals Providen")
    for i, rule in enumerate(rules):
        resReg = re.search("(=>)|(<=>)", rule)
        if not resReg:
            error("Wrong rules provided at:", line = rule)
        if resReg.group(1): # Implies `=>` found
            group = divideRule(rule, "=>") + ['!ssi']
        if resReg.group(2): # If and Only If `<=>` si et seulement si 
            group = divideRule(rule, "<=>") + ['ssi'] # ssi mean if and only if
        if bracket(group[0]) or bracket(group[1]) == -1:
            error('Wrong paranthesis', rule)
        s = group[0] + '^' + group[1]
        for v in re.split(r'[\^\|\+]', s.replace('(', '').replace(')', '').replace('!', '')):
            if (v):
                dic[v] = { 'value': default }
            else:
                error("Wrong rules provided at", line = rule)
            match = group[0].find(v)
            # print(v, group[0], group[1])
            # print(group[0].replace(v, '#' + v +'#'))
            if not re.search(r'[A-Z0-9]#[A-Z0-9]',  group[0].replace(v, '#' + v +'#')):
                group[0] = group[0].replace(v, '#' + v +'#');
            if not re.search(r'[A-Z0-9]#[A-Z0-9]',  group[1].replace(v, '#' + v +'#')):
                group[1] = group[1].replace(v, '#' + v +'#');
        if re.search(r"and|or|not|False|True", group[0]) or re.search(r"and|or|not", group[1]):
            error("Wrong name of input", line = rule)
        group[0] = group[0].replace('|', ' or ').replace('+', ' and ').replace('!', ' not ')
        group[1] = group[1].replace('|', ' or ').replace('+', ' and ').replace('!', ' not ')
        rules[i] = group
    try:
        setdic(dic, facts)
    except:
        error('Goal is useless')
    return facts, goals, rules, dic